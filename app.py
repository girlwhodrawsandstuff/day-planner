from flask import Flask, render_template, redirect, request, redirect, url_for, session
from tempfile import mkdtemp
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref
from helpers import login_required
from google.oauth2 import id_token
from google.auth.transport import requests
from flask_uploads import UploadSet, IMAGES
import base64

app = Flask(__name__)

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configurations for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planner.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# configurations for image upload
photos = UploadSet('photos', IMAGES)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    tasks = db.relationship('Todo', backref='owner')
    images = db.relationship('Images', backref='owner')
    notes = db. relationship('Notes', backref='owner')
    
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(1000), nullable=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Images(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    data = db.Column(db.LargeBinary, nullable=False) 
    rendered_data = db.Column(db.Text, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
@app.route("/")
def index():
    # redirect to login
    return redirect(url_for("login"))

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # forget any user_id
    session.clear()

    # user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        pass1 = request.form.get("password")
        pass2 = request.form.get("confirmation")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        
        # query database for usernames
        rows = Users.query.filter_by(username=username).count()
        
        # ensure username is distinct
        if rows != 0:
            return "Username is already taken"
        
        # check for matching passwords
        elif pass1 != pass2:
            return "Passwords don't match"
        
        else:
            # adding values to the table
            register = Users(username = username, password = pass1, first_name = first_name, last_name = last_name)
            db.session.add(register)
            db.session.commit()
            
            return redirect(url_for("login"))
        
    else:
        return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # forget any user_id
    session.clear()
    
    # user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        
        # ensure username was submitted
        if not request.form.get("username"):
            return "You must provide username"
        
        # ensure password was submitted
        elif not request.form.get("password"):
            return "You must provide password"
        
        username = request.form.get("username")
        password = request.form.get("password")
        
        # query database for user
        user = Users.query.filter_by(username=username, password=password).first()
        if user is not None:
        # Remember which user has logged in
            session["user_id"] = user.id
            return redirect(url_for("tasks"))
        return "Invalid username/password"
    
    else:
        return render_template("login.html")

@app.route("/googlesignin", methods=["GET", "POST"])
def tokenSignIn():
    if request.method == "POST":
        try:
            idtoken = request.form.get("idtoken")
            clientid = "178100631317-7kk5edr08pptqi100dp344ug1mhc3thi.apps.googleusercontent.com"
            print(idtoken)
            idinfo = id_token.verify_oauth2_token(idtoken, requests.Request(), clientid)
            username = str(idinfo['sub'])
            full_name = str(idinfo['name'])
            print(full_name)
            split_name = full_name.split(' ')
            first_name = split_name[0]
            if split_name[1] is not None:
                last_name = split_name[1]
            else:
                last_name=" "
            password = "defaultpassword"

            # query database for usernames
            rows = Users.query.filter_by(username=username).count()
            user = Users.query.filter_by(username=username, password=password).first()

            # check if user exists
            if rows != 0:
                if user is not None:
                    session["user_id"] = user.id
                    print("welcome back!")
                    return redirect(url_for("tasks"), 303)
            else:
                # adding values to the table
                register = Users(username = username, password = password, first_name=first_name, last_name=last_name)
                db.session.add(register)
                db.session.commit()
                print("success!")
                return redirect(url_for("tasks"))
        except:
            return "error"

@app.route("/profile", methods=["GET"])
@login_required
def profile():
    """User Profile"""
    current_user = Users.query.filter_by(id=session["user_id"]).first().username
    first_name = Users.query.filter_by(id=session["user_id"]).first().first_name
    last_name = Users.query.filter_by(id=session["user_id"]).first().last_name
    full_name = str(first_name) + " " + str(last_name)
    image = Images.query.filter_by(id=session["user_id"]).first()
    return render_template("profile.html", username=current_user, full_name=full_name, user_image=image)

def render_picture(data):
    render_pic = base64.b64encode(data).decode('ascii') 
    return render_pic

@app.route("/upload-image", methods=["GET", "POST"])
@login_required
def uploadImage():
    print('asdf')
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            print(image)
            data = image.read()
            render_file = render_picture(data)

            new_image = Images(name=image.filename, data=data, rendered_data=render_file, owner_id=session["user_id"])
            db.session.add(new_image)
            db.session.commit() 

        return redirect(url_for("profile"))

@app.route("/tasks", methods=["GET"])
@login_required
def tasks():
    """User tasks"""
    todo_list = Todo.query.filter_by(owner_id=session["user_id"])
    print(todo_list)
    return render_template("tasks.html", todo_list=todo_list)

@app.route("/add-task", methods=["POST"])
def addToTasks():
    """Add new item"""
    title = request.form.get("title")
    new_todo = Todo(title=title, owner_id=session["user_id"])
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("tasks"))

@app.route("/delete-task/<int:todo_id>")
def deleteFromTasks(todo_id):
    """Delete tasks"""
    todo_item = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo_item)
    db.session.commit()
    return redirect(url_for("tasks"))

@app.route("/calendar", methods=["GET"])
@login_required
def calendar():
    """Display calendar"""
    return render_template("calendar.html")

@app.route("/notes", methods=["GET"])
@login_required
def notes():
    """User notes"""
    return render_template("notes.html")

@app.route("/add-note", methods=["POST"])
def addNote():
    """Add new note"""
    title = request.form.get("title")
    body = request.form.get("body")
    new_note = Notes(title=title, body=body, owner_id=session["user_id"])
    db.session.add(new_note)
    db.session.commit()
    return redirect(url_for("notes"))


@app.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    """ Change password """
    if request.method == "POST":
        old = request.form.get("old")
        npass1 = request.form.get("new")
        npass2 = request.form.get("confirmation")
        
        if not request.form.get("old"):
            return "You must fill in all boxes"
            
        elif not request.form.get("new"):
            return "You must fill in all boxes"
        
        elif not request.form.get("confirmation"):
            return "You must fill in all boxes"
        
        # ensure passwords match
        elif npass1 != npass2:
            return "Passwords don't match"
        
        else:
            # adding new values to the table
            change = Users.query.filter_by(id=session["user_id"]).first()
            change.password = npass1
            db.session.commit()
            return redirect(url_for("tasks"))
        
    else:
        return render_template("settings.html")

@app.route("/logout")
@login_required
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect(url_for("login"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host="localhost", port=5000)
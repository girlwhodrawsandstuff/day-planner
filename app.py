from flask import Flask, flash, render_template, redirect, request, redirect, url_for, session
from tempfile import mkdtemp
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from helpers import login_required

app = Flask(__name__)

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configurations for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planner.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;
db = SQLAlchemy(app)

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    
class todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))

    
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
        
        # query database for usernames
        rows = users.query.filter_by(username=username).count()
        
        # ensure username is distinct
        if rows != 0:
            flash("Username is already taken")
        
        # check for matching passwords
        elif pass1 != pass2:
            flash("Passwords don't match")
        
        else:
            # adding values to the table
            register = users(username = username, password = pass1)
            db.session.add(register)
            db.session.commit()
            
            flash("Registered!")
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
            flash("You must provide username")
            return render_template("login.html")
        
        # ensure password was submitted
        elif not request.form.get("password"):
            flash("You must provide password")
            return render_template("login.html")
        
        username = request.form.get("username")
        password = request.form.get("password")
        
        # query database for user
        user = users.query.filter_by(username=username, password=password).first()
        if user is not None:
        # Remember which user has logged in
            session["user_id"] = user.id
            return redirect(url_for("tasks"))
        flash("Invalid username/password")
    
    else:
        return render_template("login.html")

@app.route("/tasks", methods=["GET"])
@login_required
def tasks():
    """User tasks"""
    # show all todos
    todo_list = todo.query.all()
    print(todo_list)
    return render_template("tasks.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
@login_required
def add():
    """Add new item"""
    title = request.form.get("title")
    new_todo = todo(title=title)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("tasks"))

@app.route("/delete/<int:todo_id>")
@login_required
def delete(todo_id):
    # delete item
    todo_item = todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo_item)
    db.session.commit()
    return redirect(url_for("tasks"))

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect(url_for("login"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
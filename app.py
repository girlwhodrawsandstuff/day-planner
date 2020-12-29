from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from tempfile import mkdtemp
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_url_path='/static')

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config['SESSION_TYPE'] = 'filesystem'
app.config["SESSION_PERMANENT"] = False
Session(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planner.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    """Redirect user"""
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()
    if request.method == "GET":
        return render_template("register.html")
    
    """TODO"""
    
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # forget any user_id
    session.clear()
    
    # user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))
        # validate username/password
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return "Invalid username or password."
        
        session["user_id"] = rows[0]["id"]
        return "Success!"
    
    # user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template('login.html')
    

@app.route('/tasks')
def tasks():
    """User tasks"""
    return render_template('tasks.html')
    """TODO"""
    
@app.route("/settings")
def settings():
    """Change password"""
    return render_template('settings.html')
    """TODO"""
    
@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")
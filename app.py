from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from tempfile import mkdtemp

app = Flask(__name__)

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

@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Sign up user"""
    session.clear()
    
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    # forget any user_id
    session.clear()
    return render_template("login.html")
    

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')
    
@app.route("/settings")
def settings():
    """Change password"""
    """TODO"""
    
@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")
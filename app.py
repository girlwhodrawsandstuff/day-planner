from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from tempfile import mkdtemp
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config['SESSION_TYPE'] = 'filesystem'
app.config["SESSION_PERMANENT"] = False
Session(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planner.db'
db = SQLAlchemy(app)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Sign up user"""
    session.clear()
    """TODO"""
    
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    session.clear()
    """TODO"""

@app.route('/')
@login_required
def index():
    return render_template('index.html')
    
@app.route("/settings")
@login_required
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
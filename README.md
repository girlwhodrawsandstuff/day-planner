# Day Planner Website
This is a Flask program where users can login and keep track of their daily tasks. In the future, I plan to add in more features like a user profile, login with Github, etc.

## Features:
1. Sign Up
2. Login/Logout
3. Change Password
4. Tasks
5. Calendar
6. Notes
7. Profile

## Demo

[![Day Planner Website](https://img.youtube.com/vi/ZX5aYcg5F8o/0.jpg)](http://www.youtube.com/watch?v=ZX5aYcg5F8o "Day Planner Website")

## Setup

1. Download/clone this project on your machine

2. [Download Python (3.7 or later)](https://www.python.org/downloads/) 

3. Install dependencies:
```Powershell
pip3 install -r requirements.txt
```

4. Set up virtualenv
```Powershell
python3 -m pip install virtualenv
python3 -m virtualenv env
source env/bin/activate
```

5. Run the app
```Powershell
$env:FLASK_ENV = "development" # or "export FLASK_ENV=development" in Linux
flask run 
```

6. Access the app locally on http://localhost:5000/



> **Note**
> 
> - In order to sign in using Google, you must use http://localhost:5000/ instead of http://127.0.0.1:5000/
> 
> - Google Sign In works with Chrome but not Mozilla Firefox.
> 

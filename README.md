# Day Planner Website
This is a Flask program where users can login and keep track of their daily tasks. In the future, I plan to add in more features like a user calendar, notes, and a login via Facebook/Google.

## Features:
1] Sign Up

2] Login/Logout

3] Change Password

4] Tasks

## Demo:
Youtube: https://youtu.be/ZX5aYcg5F8o

## Installation:

1] Clone the repository to your machine.

2] Download python(3.7 or later) from: https://www.python.org/downloads/

3] Run the following commands:
  - pip3 install pytest (not needed right now)
  - pip install -U Flask
  - pip install -U flask_session
  - pip3 install -U Jinja2 (not needed right now)
  - pip install -U Flask-SQLAlchemy
  - pip install -U Werkzeug
  - pip install -U flask-login
  - pip install -U virtualenv
  - virtualenv env
  - source env/bin/activate
  OR 
  - venv\scripts\activate
  - pip install -U google-api-python-client
  - pip install -U google-auth google-auth-oauthlib google-auth-httplib2
  - pip install -U upgrade requests

4] Once all the dependancies have been installed, run the command `python app.py`

5] This should start a local server and you can access it on your browser.
   Note: In order to sign in using Google, you must use 'http://localhost:5000/' instead of 'http://127.0.0.1:5000/'

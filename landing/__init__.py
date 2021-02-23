import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
csrf = CSRFProtect(app)

db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
dburi = 'sqlite:///{}'.format(db_path) # tells Flask and SQLAlchemy where the db will be stored

# secret key
# wtf csrf secret key
app.config.update(dict(SECRET_KEY='2809a477-5087e-4043-b9d9-a971c0982e48d', WTF_CSRF_SECRET_KEY='4cb681ac-1afe1278f84d-c8e2-4e75-ba17-1afe1278f84d', SQLALCHEMY_DATABASE_URI=dburi))

db = SQLAlchemy(app)



from .views import *
from .home.views import *
from .jobs.views import *
from .profiles.views import *
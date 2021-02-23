from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

# secret key
# wtf csrf secret key
app.config.update(dict(SECRET_KEY='2809a477-5087e-4043-b9d9-a971c0982e48d', WTF_CSRF_SECRET_KEY='4cb681ac-1afe1278f84d-c8e2-4e75-ba17-1afe1278f84d'))

from .views import *
from .home.views import *
from .jobs.views import *
from .profiles.views import *
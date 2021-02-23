from landing import db

class EmailSignup(db.Model):
    id          = db.Column(db.Integer)
    full_name   = db.Column(db.String(120), nullable=True)
    email       = db.Column(db.String(120), unique=True, nullable=False)
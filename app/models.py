from app import db
import hashlib, os

from flask_login import UserMixin
from app import login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(192))
    permission_level = db.Column(db.Integer, default=1)

    def set_password(self, password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        self.password_hash = salt+pwdhash.hex().encode('ascii')

    def check_password(self, password):
        salt = self.password_hash[:64] #stored salt
        spwd = self.password_hash[64:] #stored password(hash)
        hpwd = hashlib.pbkdf2_hmac('sha512',password.encode('utf-8'),salt,100000)
        return spwd == hpwd.hex().encode('ascii')

    def __repr__(self):
        return '<User {}>'.format(self.username) 

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
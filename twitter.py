
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_login import LoginManager, login_manager
import os

app = Flask(__name__)
photos = UploadSet('photos', IMAGES)
app.config["UPLOADED_PHOTOS_DEST"] = os.getcwd()
app.config["SECRET_KEY"] = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:12345678@localhost/twitter"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOADED_PHOTOS_ALLOW"] = ["jfif","jpg", "jpeg"]
configure_uploads(app, photos)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@app.template_filter('time_since')
def time_since(delta):
    seconds = delta.total_seconds()
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    if days > 0:
        return '%dd' % (days)
    if hours > 0:
        return '%dh' % (hours)
    if minutes > 0:
        return '%dm' % (minutes)
    if seconds > 0:
        return 'Just now'

from views import *
    
    
if __name__ == "__main__":
    app.run(debug = True)
from app.app_and_db import db


class Image(db.Model):
    __tablename__ = "image"
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(255))
    location = db.Column(db.String(255))
    lat = db.Column(db.Integer)
    lon = db.Column(db.Integer)
    add_at = db.Column(db.DateTime())
    size = db.Column(db.Integer)
    likes = db.relationship("Like", backref="image")

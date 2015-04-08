from app.app_and_db import db


class Image(db.Model):
    __tablename__ = "image"
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(255))
    location = db.Column(db.String(255))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    add_at = db.Column(db.DateTime())
    published_at = db.Column(db.DateTime())
    size = db.Column(db.Float)
    desc = db.Column(db.Text)
    title = db.Column(db.String(255))
    likes = db.relationship("Like", backref="image")

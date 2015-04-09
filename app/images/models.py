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

    @classmethod
    def latest_images(self, count = 6):
        images = {}
        for counter, image in enumerate(db.session.query(Image).order_by(Image.add_at).limit(count)):
            images[counter] = image

        return images

    @classmethod
    def favourite_images(self, count = 6):
        images = {}
        
        # for counter, image in enumerate(db.session.query(Image).join(Image, Like.image_id).limit(count)):
        #     images[counter] = image

        return images 
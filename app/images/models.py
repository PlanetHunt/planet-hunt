from app.app_and_db import db
import app.likes as likes

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
    source = db.Column(db.Text)
    license = db.Column(db.String(255))
    title = db.Column(db.String(255))
    likes = db.relationship("Like", backref="image")

    @classmethod
    def latest_images(self, count=6):
        images = {}
        for counter, image in enumerate(db.session.query(Image)
                                        .order_by(Image.add_at).limit(count)):
            images[counter] = image

        return images

    @classmethod
    def favourite_images(self, count=6):
        images = {}

        # for counter, image in enumerate(db.session.query(Image).join(Image, Like.image_id).limit(count)):
        #     images[counter] = image

        return images

    @classmethod
    def query_image(self, count, offset):
        return db.session.query(Image).order_by(Image.add_at).limit(count).\
            offset(offset)

    @classmethod
    def get_untouched_image(self, user_id, count=10, offset=0):
        tagged_images = []
        result_images = []
        offset = offset
        res = likes.models.Like.get_user_likes(user_id)
        for r in res:
            tagged_images.append(r.id)
        images = self.query_image(count, offset)
        for im in images:
            if im.id not in tagged_images:
                result_images.append(im)
        while len(result_images) < 1:
            offset = offset + 5
            images = self.query_image(count, offset)
            for im in images:
                if im.id not in tagged_images:
                    result_images.append(im)
        return result_images

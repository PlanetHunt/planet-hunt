from app.app_and_db import db
import app.images as images


class Like(db.Model):
    __tablename__ = "like"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))
    negate = db.Column(db.Integer)

    @classmethod
    def get_user_likes(self, user_id):
        return db.session.query(Like).filter(Like.user_id == user_id)

from flask import render_template, request, jsonify
from flask_user import login_required, current_user
from app.images.models import Image
from app.likes.models import Like
from app.app_and_db import app, db


@app.route('/likes/')
def likes_page():
	return render_template('likes/likes_index_page.html', images=1)


@app.route('/test')
@login_required
def test_page():
	images = Image.get_untouched_image(current_user.id)
	a = len(images)
	return render_template('likes/likes_test_page.html', images=a)

@app.route('/_add_like')
@login_required
def add_like():
	image_id = request.args.get('image_id', 0, type=int)
	negate = request.args.get('negate', 0, type=int)
	user_id = current_user.id
	like = Like()
	like.user_id = user_id
	like.image_id = image_id
	like.negate = negate
	return jsonify(result = user.id)

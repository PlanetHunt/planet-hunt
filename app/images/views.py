# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import redirect, render_template, request, url_for
from flask_user import login_required, roles_required
from app.images.models import Image
from app.app_and_db import app,db

@app.route('/images/')
def images_page():
	paths = []

	for image in db.session.query(Image).all():
		paths.append(image.path)

	return render_template('images/images_index_page.html', paths=paths)

@app.route('/image/')
@app.route('/image/<id>')
def image_page(id=None, image_path=None):
	for image in db.session.query(Image).filter(Image.id == id):
		image_path = image.path

	return render_template('images/image_view_page.html', id=id, image_path = image_path)
# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import render_template
from flask_user import login_required, roles_required
from app.images.models import Image

from app.app_and_db import app


# The Home page is accessible to anyone
@app.route('/')
def home_page():

    return render_template('pages/home_page.html', 
    	latest_images = Image.latest_images(3),
    	favourite_images = Image.favourite_images(3))

# The Member page is accessible to authenticated users (users that have logged in)
@app.route('/member')
@login_required             # Limits access to authenticated users
def member_page():
    return render_template('pages/member_page.html')

# The Admin page is accessible to users with the 'admin' role
@app.route('/admin')
@roles_required('admin')    # Limits access to users with the 'admin' role
def admin_page():
    return render_template('pages/admin_page.html')

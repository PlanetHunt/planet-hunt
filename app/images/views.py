# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import render_template
from flask_user import login_required, roles_required

from app.app_and_db import app


# The Home page is accessible to anyone
@app.route('/')
def home_page():
    return render_template('pages/images/index_page.html')

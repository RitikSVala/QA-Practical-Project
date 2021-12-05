

from app import app, db
from flask import render_template, request
from app.models import Rapper
from flask import request


# import sqlite3

###
# Routing for your application.
###

# Service 3
@app.route('/date-api', methods=['POST'])
def get_random_number():
    rapper_id = int(request.form.get('id'))
    rapper = db.session.query(Rapper).filter_by(id=rapper_id).first()
    return {"date": rapper.birth_date}


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404



from app import app, db
from flask import render_template, request
from app.models import Rapper
from flask import request



###
# Routing for application.
###

# Service 4
@app.route('/display-api', methods=['POST'])
def get_final_results():
    rapper_id = int(request.form.get('id'))
    rapper = db.session.query(Rapper).filter_by(id=rapper_id).first()
    return {"data": 'Your Rapper name is    %r   Your best album was released in   %r ' % (rapper.name, rapper.birth_date)}


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

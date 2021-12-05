
from app import app, db
from flask import render_template, request
from app.models import Rapper
import random
from flask import request




###
# Routing for application.
###

@app.route('/', methods=['POST', 'GET'])
def home():
    """Render website's home page."""

    if request.method == 'POST':
        rappers = db.session.query(Rapper).all()

        return render_template('home.html', rappers=random.choice(rappers))

    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


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

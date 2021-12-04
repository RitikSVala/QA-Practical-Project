"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import InputForm
from app.models import Rapper
import random
from flask import request


# import sqlite3

###
# Routing for your application.
###

# Service 2
@app.route('/name-api', methods=['GET'])
def get_rapper():
    rapper = random.choice(db.session.query(Rapper).all())
    return {"result": rapper.name, "id": rapper.id}

@app.route('/rappers')
def show_rappers():
    rappers = db.session.query(Rapper).all()  # or you could have used User.query.all()

    return render_template('show_rappers.html', rappers=rappers)


@app.route('/add-rapper', methods=['POST', 'GET'])
def add_rapper():
    '''
    Input form validates the input, makes sure it is not blank 
    '''
    input_form = InputForm()

    if request.method == 'POST':
        if input_form.validate_on_submit():
            # Get validated data from form
            name = input_form.name.data  # You could also have used request.form['name']
            birth_date = input_form.birth_date.data
            # save user to database
            user = Rapper(name, birth_date)
            db.session.add(user)
            db.session.commit()

            flash('Rapper successfully added')
            return redirect(url_for('show_rappers'))

    flash_errors(input_form)
    return render_template('add_rapper.html', form=input_form)


# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))


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

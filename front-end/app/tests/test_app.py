import random
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import sys
sys.path.append('../')
from app.models import Rapper

from app import app

app.config['SECRET_KEY'] = 'super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testDatabase.db'
test_db = SQLAlchemy(app)

from flask import Flask, request
import os
import tempfile


import pytest

with app.test_request_context('/'):
    assert request.path == '/'

def test_add_rapper():
    # Insert rapper to the database
    rapper = Rapper("Test1","1 Jan,2000")
    test_db.session.add(rapper)
    test_db.session.commit()

    # Retrieve rapper from test database
    rapper = test_db.session.query(Rapper).first()

    # Delete rapper after testing is done
    test_db.session.delete(rapper)
    test_db.session.commit()
    assert rapper.name == "Test1"

def test_retrieve_rappers():
    rapper1 = Rapper("Test2","2 June, 2003")
    rapper2 = Rapper("Test3","14 Feb, 1997")
    rapper3 = Rapper("Test4","10 Oct, 1995")

    test_db.session.add(rapper1)
    test_db.session.commit()

    test_db.session.add(rapper2)
    test_db.session.commit()

    test_db.session.add(rapper3)
    test_db.session.commit()
    

    rappers = test_db.session.query(Rapper).all()

    test_db.session.delete(rapper1)
    test_db.session.commit()

    test_db.session.delete(rapper2)
    test_db.session.commit()

    test_db.session.delete(rapper3)
    test_db.session.commit()
    if len(rappers) == 3 :
        assert True
    else:
        assert False
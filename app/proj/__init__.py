"""
Be careful with circularity.
"""
__author__ = 'donal'
__project__ = 'ribcage'

# to be used in views -
from flask import Blueprint
proj = Blueprint('proj', __name__)

# needs to go last (coming back from views) -
from . import views
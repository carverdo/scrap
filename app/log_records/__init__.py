__author__ = 'donal'
__project__ = 'ribcage'

from flask import Blueprint
log_recs = Blueprint('log_recs', __name__)
from . import views
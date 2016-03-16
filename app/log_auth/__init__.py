__author__ = 'donal'
__project__ = 'ribcage'

from flask import Blueprint
log_auth = Blueprint('log_auth', __name__)
# goes last
from . import views, view_errors
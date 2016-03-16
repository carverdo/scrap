__author__ = 'donal'
__project__ = 'ribcage'

from flask import render_template
from ..log_auth.views import login_confirmed
from . import proj

# ========================
# SIMPLE STUFF
# ========================
@proj.route('/')
@proj.route('/home2')
@login_confirmed
def home2():
    return render_template('./proj/dummy.html')







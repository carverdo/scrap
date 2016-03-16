__author__ = 'donal'
__project__ = 'ribcage'

from flask import current_app
from . import log_recs
from ..log_auth.views import admin_required, set_template

@log_recs.route('/logs')
@admin_required
def logs():
    txt = open('logs/Devel_logs.log').readlines()
    return set_template('panelbuilder.html', txt, '',
                        panel_args=dict(
                                patex=current_app.config['PAHDS']['logs'],
                                tadata=current_app.config['TADATA']['logs'],
                                wid=12
                        ))

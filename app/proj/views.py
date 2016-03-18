__author__ = 'donal'
__project__ = 'ribcage'

from flask import render_template, current_app, request, redirect, url_for
from sqlalchemy import desc
from ..log_auth.views import login_confirmed, set_template
from app.db_models import BibleBlock
from . import proj
from forms import BibleFo
# ========================
# SIMPLE STUFF
# ========================
@proj.route('/')
@proj.route('/home2')
@login_confirmed
def home2():
    return render_template('./proj/dummy.html')


@proj.route('/bible')
@login_confirmed
def bible():
    # Row click activates detail for member
    try: return redirect(url_for('.cp_detail', m_id = request.args.get('m')))
    except: pass
    all_data = BibleBlock.query.order_by(BibleBlock.id)
    return set_template('panelbuilder.html', all_data, '.bible',
                        panel_args=dict(
                            patex=current_app.config['PAHDS']['bible'],
                            tadata=current_app.config['TADATA']['bible'],
                            wid=12
                        ))


@proj.route('/cp_detail/<m_id>', methods=["GET", "POST"])
@login_confirmed
def cp_detail(m_id):
    all_data = BibleBlock.query.filter_by(corp=m_id).first()
    if request.method == 'POST':
        all_data.update(**dict(request.form.items()))
        all_data = BibleBlock.query.filter_by(corp=m_id).first()
    form = BibleFo()
    form.get_existing_data(all_data)
    return set_template('panelbuilder.html', form, '.cp_detail',
                        panel_args=dict(
                            patex=current_app.config['PAHDS']['bible'],
                            tadata=current_app.config['TADATA']['INDIbible'],
                            wid=12
                        ),
                        kwargs={'m_id':m_id}
                        )

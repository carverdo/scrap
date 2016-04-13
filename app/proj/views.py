__author__ = 'donal'
__project__ = 'ribcage'

from flask import render_template, current_app, request, redirect, url_for
from flask.ext.login import current_user
from ..log_auth.views import login_confirmed, set_template
from app.db_models import BibleBlock, PersonalNotes
from . import proj
from forms import BibleFo, FALSE_RANK, INSTANTI_RANK

# ========================
# SIMPLE STUFF
# ========================
@proj.route('/')
@proj.route('/home2')
@login_confirmed
def home2():
    return render_template('./proj/dummy.html')


@proj.route('/bible', methods=["GET", "POST"])
@login_confirmed
def bible():
    # Row click activates detail for member
    try: return redirect(url_for('.cp_detail', c_id = request.args.get('c')))
    except: pass
    all_data = BibleBlock.query.order_by(BibleBlock.id).all()
    # we gather personal ranking data for sorting
    p_ranks = [filter(lambda x:
                      x.member_id==current_user.id, ro.personal_notes
                      ) for ro in all_data]
    p_ranks = map(lambda x: x[0].myRank if x else FALSE_RANK, p_ranks)
    return set_template('panelbuilder.html', zip(p_ranks, all_data), '.bible',
                        panel_args=dict(
                            patex=current_app.config['PAHDS']['bible'],
                            tadata=current_app.config['TADATA']['bible'],
                            wid=12
                        ))


@proj.route('/cp_detail/<c_id>', methods=["GET", "POST"])
@login_confirmed
def cp_detail(c_id):
    form = BibleFo()
    # call existing data
    all_data = BibleBlock.query.filter_by(corp=c_id).first()
    test_existing_pnotes = PersonalNotes.query.filter_by(
            member_id=current_user.id, bblock_id=all_data.id).count()
    # create a blank on first call -
    if not test_existing_pnotes:
        PersonalNotes(member_id=current_user.id, bblock_id=all_data.id,
                      myRank=INSTANTI_RANK, readUrl='n').update()
    pers_notes = PersonalNotes.query.filter_by(
            member_id=current_user.id, bblock_id=all_data.id).first()
    # update for posts
    if request.method == 'POST':
        if form.validate():
            all_data.update(**dict(request.form.items()))
            pers_notes.update(**dict(request.form.items()))
    # instantiate our form object for presentation
    form.get_existing_data(all_data)
    form.get_existing_data(pers_notes)
    return set_template('panelbuilder.html', form, '.cp_detail',
                        panel_args=dict(
                            patex=current_app.config['PAHDS']['bible'],
                            tadata=current_app.config['TADATA']['INDIbible'],
                            wid=12
                        ),
                        kwargs={'c_id': c_id}
                        )

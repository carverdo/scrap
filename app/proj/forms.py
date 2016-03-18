__author__ = 'donal'
__project__ = 'funding_bible'

from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, validators
# PasswordField, BooleanField, SelectField, validators, IntegerField
from config_vars import MAX_COL_WIDTHS, MIN_PASS_LEN

class BibleFo(Form):
    """
    Inherit (from signup), modify (including default in model),
    and auto-present the pre-populated forms data.
    """
    tag = StringField("tag")
    corp = StringField("corp")
    url = StringField("url")
    city = StringField("city")
    country = StringField("country")
    # next row
    investmentPhase = StringField("investmentPhase")
    geoFocus = StringField("geoFocus")
    sectorFocus = StringField("sectorFocus")
    minInv = StringField("minInv")
    maxInv = StringField("maxInv")
    dealCount = StringField("dealCount")
    aum = StringField("aum")
    # and next
    dealList  = TextAreaField("dealList")
    established  = StringField("established")
    connectedNames  = TextAreaField("connectedNames")
    description  = TextAreaField("description")

    def get_existing_data(self, member):
        # user-entry data
        for k, v in member.__dict__.items():
            try:
                self.__dict__[k].default = v
                # print self.__dict__[k].validate(self)
            except: pass
        # process those changes
        self.process()

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True

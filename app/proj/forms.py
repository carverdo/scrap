__author__ = 'donal'
__project__ = 'funding_bible'
#todo add field validations

from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, IntegerField, validators
# PasswordField, BooleanField, SelectField,
from config_vars import MAX_COL_WIDTHS, MIN_PASS_LEN

FALSE_RANK = 10000
INSTANTI_RANK = 5000


class BibleFo(Form):
    """
    Is used in for two data tables (private and public)
    """
    # personal data
    myNotes = StringField("myNotes")
    myRank = IntegerField(
            "myRank",
            [validators.InputRequired('You need to enter a number into myRank'),
             validators.NumberRange(min=0, max=FALSE_RANK)],
            default=INSTANTI_RANK
    )
    readUrl = StringField("readUrl")
    # basics
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

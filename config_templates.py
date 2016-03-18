"""
Part 2 of the config -
The moving parts for the templates that you will use in your project.
"""
__author__ = 'donal'
__project__ = 'ribcage'


class TemplateParameters(object):
    PAHDS = dict(
        adm_members = 'Control Default Settings of Members',
        adm_visits = 'Member Visits (click on a row to expand)',
        profile = 'Change your Password',
        signin = 'Log in to begin...',
        signup = 'Sign up to get started',
        logs = 'Your Logged Records',
        bible = 'Our Dataset'
        # addtasks = 'Build your schedule',
        # adm_bucketmap = 'Allow bucket access: connect DB to S3',
        # balldata = 'Movement Data',
        # curtasks = 'Your scheduled tasks',
        # str_amount = 'SOME WORDS'
    )
    TADATA = dict(
        adm_members = 'log_auth/adm_members_tdata.html',
        adm_visits = 'log_auth/adm_visits_tdata.html',
        adm_INDIvisits = 'log_auth/adm_INDIvisits_tdata.html',
        profile = 'log_auth/profile_tdata.html',
        signin = 'log_auth/signin_tdata.html',
        signup = 'log_auth/signup_tdata.html',
        logs = 'log_records/log_records_tdata.html',
        bible = 'proj/bible_tdata.html',
        INDIbible = 'proj/INDIbible_tdata.html'
        # addtasks = 'xx_timer_tdata.html',
        # adm_bucketmap = 'adm_bucketmap_tdata.html',
        # balldata = 'xx_device_tracker_tdata.html',
        # curtasks = 'xx_sched_tdata.html',
        # str_amount = 'xx_stramount_tdata.html'
    )
    PANEL = dict(PAHDS=PAHDS, TADATA=TADATA)

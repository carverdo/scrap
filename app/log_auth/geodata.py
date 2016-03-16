"""
HAVE NOT TESTED FOR SPEED (but second one seems better)

Decent link here about ip spoofing -
http://esd.io/blog/flask-apps-heroku-real-ip-spoofing.html

I think it has already been incorporated
and my code works on his committed change.
"""
__author__ = 'donal'
__project__ = 'ribcage'
from json import loads
from urllib2 import urlopen
from flask import request
from flask.ext.login import current_user
from config_vars import VALID_IP


# ========================
# PRIMARY CALL
# ========================
def get_clientdata():
    # DO NOT UNDERSTAND DISTINCTIONS
    # ip = request.access_route[0] or request.remote_addr
    # ip = request.headers.getlist('X-Forwarded-For', request.remote_addr)
    # ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    client_data = {}
    ip = request.environ.get('REMOTE_ADDR', request.remote_addr)
    if not VALID_IP.match(ip):
        raise ValueError('Invalid IPv4 format')
    client_data['ip_address'] = ip
    client_data['browser'] = request.headers.get("User-Agent")
    if current_user.is_active:
        client_data['member_id'] = current_user.get_id()
    return client_data

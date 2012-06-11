# coding=utf-8
 
import os

debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')
debug_profiler_enabled = False
appname = 'WebPutty OSS'
appversion_raw = [1, 3, 0]
appversion = '.'.join([str(num) for num in appversion_raw])
invite_sender_email = '%s Invitation <martin.cap78@googlemail.com>' % appname
incoming_sender_email = '%s Incoming Mail <martin.cap78@googlemail.com>' % appname
log_all_incoming = True
# List of admins to forward mail to.
forward_mail_to = ['martin.cap78@googlemail.com']
jquery_url = '//ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js'
# Generate this once by calling os.urandom(24)
secret_key = "mtype"

# Name of the Google Cloud Storage bucket
use_google_cloud_storage = False
google_bucket = 'yourbucket'

available_locales = [
    ('en', u'English'),
    ('fr', u'Français'),
]

# API Keys for url2png.com
url2png = dict(
    user = 'USERNAME',
    password = 'PASSWORD',
    bounds = '300x300',
)


# -*- coding: utf-8 -*-
from django.conf import settings

default_settings = {
    'MAILCHIMP_CLIENT_ID': None,
    'MAILCHIMP_CLIENT_SECRET': None,

    'MAILCHIMP_AUTHORIZATION_URL': 'https://login.mailchimp.com/oauth2/authorize',
    'MAILCHIMP_ACCESS_TOKEN_URL': 'https://login.mailchimp.com/oauth2/token',
    'MAILCHIMP_METADATA_URL': 'https://login.mailchimp.com/oauth2/metadata',
    'MAILCHIMP_SUCCESS_REDIRECT_URL': '/',
}


class Settings(object):
    def __init__(self, app_settings, defaults):
        for k, v in defaults.iteritems():
            setattr(self, k, getattr(app_settings, k, v))

settings = Settings(settings, default_settings)

# -*- coding: utf-8 -*-

import urllib

import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from . import settings
from .models import MailChimpUser


class MailChimpAuthView(RedirectView):
    permanent = True

    text_error = 'Attempt to authenticate has failed. Please try again.'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MailChimpAuthView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        if not code:
            return self.authorize_uri_request()

        response = self.access_token_uri_request(code)
        if not response.status_code == 200:
            return self.error_message()

        response_data = response.json()
        access_token = response_data.get('access_token')
        if not access_token:
            return self.error_message()

        response = self.metadata_uri_request(access_token)
        if not response.status_code == 200:
            return self.error_message()

        metadata = response.json()

        chimp, _ = MailChimpUser.objects.get_or_create(chimp=request.user)
        chimp.access_token = access_token
        chimp.metadata = metadata
        chimp.save()

        messages.add_message(request, messages.SUCCESS, 'Your account has been successfully updated with '
                                                        'MailChimp.')

        return self.complete()

    def authorize_uri_request(self):
        params = urllib.urlencode({
            'client_id': settings.MAILCHIMP_CLIENT_ID,
            'redirect_uri': self.request.build_absolute_uri(reverse('mailchimp_auth')),
            'response_type': 'code',
        })

        return self.complete(settings.MAILCHIMP_AUTHORIZATION_URL + '?' + params)

    def access_token_uri_request(self, code):
        headers = {
            'User-Agent': 'oauth2-draft-v10',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        params = {
            'client_id': settings.MAILCHIMP_CLIENT_ID,
            'client_secret': settings.MAILCHIMP_CLIENT_SECRET,
            'code': code,
            'grant_type': 'authorization_code',
            'redirect_uri': self.request.build_absolute_uri(reverse('mailchimp_auth')),
        }

        return requests.post(url=settings.MAILCHIMP_ACCESS_TOKEN_URL, data=params, headers=headers)

    def metadata_uri_request(self, access_token):
        return requests.get(url=settings.MAILCHIMP_METADATA_URL, headers=self.oauth_header(access_token))

    def oauth_header(self, token):
        """
        MailChimp's docs prescribe This header is the 'magic' that makes this
        empty GET request work.
        """
        return {'Authorization': 'OAuth %s' % token}

    def error_message(self, msg=text_error):
        messages.add_message(self.request, messages.ERROR, '%s' % msg)
        return self.complete()

    def complete(self, redirect=settings.MAILCHIMP_SUCCESS_REDIRECT_URL):
        return HttpResponseRedirect(redirect)

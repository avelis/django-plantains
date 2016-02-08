# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views import MailChimpAuthView

urlpatterns = patterns('',
                       url('login/', MailChimpAuthView.as_view(), name='mailchimp_auth'),
                       )

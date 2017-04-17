# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import MailChimpAuthView

urlpatterns = [
    url('login/', MailChimpAuthView.as_view(), name='mailchimp_auth'),
]

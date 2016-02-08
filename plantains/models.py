from django.conf import settings
from django.db import models

from jsonfield import JSONField


class MailChimpUser(models.Model):
    chimp = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, related_name='mailchimp_user')
    access_token = models.CharField(max_length=64, null=True)
    metadata = JSONField(null=True)

    def is_chimped(self):
        return self.access_token

    def __unicode__(self):
        return unicode(self.chimp)

    class Meta:
        db_table = 'mailchimp_user'

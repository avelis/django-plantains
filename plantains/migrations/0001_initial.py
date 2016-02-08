# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailChimpUser',
            fields=[
                ('chimp', models.OneToOneField(related_name='mailchimp_user', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('access_token', models.CharField(max_length=64, null=True)),
                ('metadata', jsonfield.fields.JSONField(null=True)),
            ],
            options={
                'db_table': 'mailchimp_user',
            },
        ),
    ]

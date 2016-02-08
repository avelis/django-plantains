# Django Plantains

Django plantains creates the ability to persist the association of a MailChimp account to an AuthUser account in Django. Leveraging the Django framework this can facitate authentication and persisted storage of Oauth metadata for later retrieval and usage.

# Requirements
Django plantains was built and tested for:
* Django: 1.8
* Python: 2.7

# Installation
Use pip to install into a virtualenv:
```shell
pip install django-plantains
```

In `settings` configuration file add the following:
```python
INSTALLED_APPS = (
    ...
    'plantains',
)
```

Include the application URLconf in your project urls.py:
```python
url(r'^plantains/', include('plantains.urls')),
```

```python
MAILCHIMP_CLIENT_ID = '123456789'
MAILCHIMP_CLIENT_SECRET = 'a1b2c3d4e5f6789'

# Optional parameters
# Defaults
MAILCHIMP_SUCCESS_REDIRECT_URL = '/'


# These are in case MailChimp decides
# to change it's endpoints
MAILCHIMP_AUTHORIZATION_URL = 'https://slack.com/oauth/authorize'
MAILCHIMP_ACCESS_TOKEN_URL = 'https://slack.com/api/oauth.access'
```

Use the authentication url to begin the Oauth process in your Django templates.
```html
<a href="{% url 'mailchimp_auth' %}">Feelin Chimpy</a>
```

Once the authentication is complete you can find your access_token in the `mailchimp_user` table.

## How to Contribute
Django-plantains is willing and open to accept all contributions. Take a fork and make a pull-request. If you feel like becoming an active maintainer, please get in touch in becoming a project contributor.

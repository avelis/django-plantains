import pypandoc
from setuptools import setup

long_description = pypandoc.convert('README.md', 'rst')

setup(
    name='django-plantains',
    version='0.1.0',
    description='Persistable oauth2 Mailchimp backend for Django.',
    long_description=long_description,
    keywords='django, mailchimp, oauth2',
    author='Andrew Velis',
    author_email='andrew.velis@gmail.com',
    url='https://github.com/avelis/django-plantains/',
    license='BSD',
    packages=[
        'plantains',
    ],
    zip_safe=False,
    install_requires=[
        'Django>=1.8.1',
        'requests',
        'jsonfield==1.0.3',
    ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

from setuptools import setup

try:
    from pypandoc import convert

    def read_md(f): return convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")

    def read_md(f): return open(f, 'r').read()

long_description = read_md('README.md')

setup(
    name='django-plantains',
    version='0.2',
    description='Persistable oauth2 Mailchimp backend for Django.',
    long_description=long_description,
    keywords='django, mailchimp, oauth2',
    author='Andrew Velis',
    author_email='andrew.velis@gmail.com',
    url='https://github.com/avelis/django-plantains/',
    license='BSD',
    packages=[
        'plantains',
        'plantains.migrations',
    ],
    zip_safe=False,
    install_requires=[
        'Django>=1.10.1',
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
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

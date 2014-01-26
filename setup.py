import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'hautomation-restclient',
    version = '0.3',
    packages = ['hautomation_restclient'],
    include_package_data = True,
    license = 'BSD License',
    description = 'Module for sending home automation commands and device management requests to django-hautomation REST API',
 #   long_description = README,
#TODO set the project's home page
    url = 'http://blog.digitalhigh.es',
    author = 'Javier Pardo Blasco(jpardobl)',
    author_email = 'jpardo@digitalhigh.es',
    install_requires = (
      "requests==1.2.0",
      "simplejson==2.6.2",
    ),
    test_suite='hautomation_restclient.tests.runtests',
    tests_require=("requests"),
    classifiers = [        
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Home Automation',
    ],
)

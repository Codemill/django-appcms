from setuptools import setup, find_packages

version = __import__('appcms').__version__

setup(
    name = 'django-appcms',
    version = version,
    description = 'Templatetags for inserting django-cms placeholders in app templates.',
    author = 'Ludvig Widman, CodeMill AB',
    author_email = 'opensource@codemill.se',
    url = 'http://github.com/codemill/django-appcms',
    packages = find_packages(),
    install_requires = [
        'django-cms>=2.4',
    ],
)

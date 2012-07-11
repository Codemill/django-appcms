# django-appcms
Templatetags for inserting django-cms placeholders in app templates. Enables front end editing of content in your apps.

## Requirements
django-cms

## Usage
- Add appcms to INSTALLED\_APPS in your settings.py file:

		INSTALLED_APPS = (
			...
			'appcms',
			'''
		)

- Load appcms\_tags in your template:

		{% load appcms_tags %}

- Add a placeholder:

		{% appcms_placeholder "name_of_placeholder" %}

- Make sure the base template includes the django-cms toolbar

When the view loads with a admin logged in editing can be enabled in the django-toolbar.

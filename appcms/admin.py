from django.contrib import admin
from appcms.models import *
from cms.admin.placeholderadmin import PlaceholderAdmin

admin.site.register(Placeholder, PlaceholderAdmin)

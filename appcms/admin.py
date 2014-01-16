from django.contrib import admin
from appcms.models import Placeholder
from cms.admin.placeholderadmin import PlaceholderAdmin


class AppCmsPlaceholderAdmin(PlaceholderAdmin):
    pass

admin.site.register(Placeholder, AppCmsPlaceholderAdmin)

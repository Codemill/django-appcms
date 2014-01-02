from django.contrib import admin
from appcms.models import *
from cms.admin.placeholderadmin import TranslatableAdmin, PlaceholderAdmin


class AppCmsPlaceholderAdmin(TranslatableAdmin, PlaceholderAdmin):

    def placeholder_plugin_filter(self, request, queryset):
        return queryset.filter(language=request.LANGUAGE_CODE)

admin.site.register(Placeholder, AppCmsPlaceholderAdmin)

from django import template
from classytags.arguments import Argument
from classytags.core import Tag, Options
from django.template.defaultfilters import safe
from ..models import Placeholder
register = template.Library()

class RenderPlaceholder(Tag):
    name = 'appcms_placeholder'
    options = Options(
        Argument('name'),
        Argument('width', default=None, required=False),
    )

    def render_tag(self, context, name, width):
        request = context.get('request', None)
        if not request:
            return ''
        if not name:
            return ''

        placeholder, created = Placeholder.objects.get_or_create(name=name)
        placeholder.placeholder.slot = name
        return safe(placeholder.placeholder.render(context, width))
register.tag(RenderPlaceholder)

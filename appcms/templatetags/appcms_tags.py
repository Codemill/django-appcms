from django import template
from classytags.arguments import Argument
from classytags.core import Tag, Options
from django.template.defaultfilters import safe
from django.core.cache import cache
from ..models import Placeholder
import hashlib

register = template.Library()


class RenderPlaceholder(Tag):
    name = 'appcms_placeholder'
    options = Options(
        Argument('name'),
        Argument('width', default=None, required=False),
    )

    def render_tag(self, context, name, width):

        def _get_placeholder(name, context, width):
            placeholder, created = Placeholder.objects.get_or_create(name=name)
            placeholder.placeholder.slot = name
            return safe(placeholder.placeholder.render(context, width))

        request = context.get('request', None)
        if not request or not name:
            return ''

        if not request.user.is_staff:
            m = hashlib.md5()
            m.update(name)
            key = 'placeholder-%s' % m.hexdigest()
            cached = cache.get(key)
            if cached:
                return cached
            else:
                resp = _get_placeholder(name, context, width)
                cache.set(key, resp, 60)
                return resp

        return _get_placeholder(name, context, width)
register.tag(RenderPlaceholder)

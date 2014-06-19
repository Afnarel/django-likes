from django import template
from likes.utils import can_vote, can_like, can_unlike, likes_enabled

register = template.Library()


@register.inclusion_tag('likes/inclusion_tags/likes_extender.html',
                        takes_context=True)
def likes(context, obj, template=None):
    if template is None:
        template = 'likes/inclusion_tags/likes.html'
    request = context['request']
    context.update({
        'template': template,
        'content_obj': obj,
        'likes_enabled': likes_enabled(obj, request),
        'can_vote': can_vote(obj, request.user, request),
        'can_like': can_like(obj, request.user, request),
        'can_unlike': can_unlike(obj, request.user, request),
        'content_type': "-".join((obj._meta.app_label, obj._meta.module_name))
    })
    return context

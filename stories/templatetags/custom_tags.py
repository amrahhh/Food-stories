from django.template import Library
from stories.models import Category
from stories.forms import SubscriberForm

register = Library()

@register.simple_tag
def get_categories(ispublished=True, n=None):
    return Category.objects.filter(is_published=ispublished)[:n]


@register.simple_tag
def get_subs():
    return SubscriberForm
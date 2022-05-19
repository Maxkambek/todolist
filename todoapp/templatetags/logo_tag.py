from django import template
from todoapp.models import Logo
register = template.Library()


@register.simple_tag
def get_logo():
    logo = Logo.objects.all().last().image.url
    print(logo)
    return logo

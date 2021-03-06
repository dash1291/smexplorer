from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def getExtension(value):
    """Gets the extension of a file"""
    return value.split(".")[-1]


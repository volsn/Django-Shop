from django import template


register = template.Library()


@register.filter(name='validate')
def validate(value):
    return value.replace(' ', '_')

@register.filter
def lower(value):
    return value.lower()

"""
register.filter('validate', validate)
register.filter('lower', lower)
"""

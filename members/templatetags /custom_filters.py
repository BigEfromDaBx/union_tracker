from django import template

register = template.Library()

@register.filter(name='last4')
def last4(value):
    """Returns the last 4 characters of the given string."""
    if value and len(value) > 4:
        return value[-4:]
    return value
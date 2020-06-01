from django import template
register = template.Library()

# the line below uses decorators

@register.filter(name='cutout')
def cutout(value, arg):
    return value.replace(arg, '')

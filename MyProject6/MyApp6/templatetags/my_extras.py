from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This Cuts Out All Values of "arg" from the string!
    """
    return value.replace(arg,'')

#register.filter('cut',cut)

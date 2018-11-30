from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string
    """

    return  value.replace(arg, '')


# The below line of code can be ommitted if the above line is used that is decorators are used. we can use either of them.
# register.filter('cut', cut)    
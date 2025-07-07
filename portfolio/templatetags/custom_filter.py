from django import template

register = template.Library()

@register.filter(name='split')
def split(value, arg):
    
    params = arg.split(",")
    delimiter = ' '
    if len(params) == 1:
        index = int(params[0])
    else:
        index = int(params[0])
        delimiter = params[1]
    
    if isinstance(value, str):
        values = value.split(delimiter)
        if index != -1:
            return values[index]
        return values
    return value
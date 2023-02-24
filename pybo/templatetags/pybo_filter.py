import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg


@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))


@register.filter
def replace_space(value, arg):
    return value.replace(" ", arg)


@register.filter
def return_ox(value):
    if value:
        return "O"
    return "X"

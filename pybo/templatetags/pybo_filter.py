import markdown
from django import template
from django.utils.safestring import mark_safe
import datetime

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


@register.filter
def sub_time(value, arg):
    if value == arg:
        return "시험을 완료 하지 않음."
    else:
        time = (value - arg).total_seconds()
        hour, minu = divmod(time, 3600)
        minu, sec = divmod(minu, 60)
    return str(int(hour)) + "시간 " + str(int(minu)) + "분 " + str(int(sec)) + "초"


@register.filter
def null_to_blank(value):
    if value:
        return value
    else:
        return ""
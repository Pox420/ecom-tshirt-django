from django import template
import math

register = template.Library()


@register.simple_tag
def get_order_status_class(status):
    if status == "COMPLETED":
        return "success"
    elif status == "PLACED":
        return "primary"
    else:
        return "warning"

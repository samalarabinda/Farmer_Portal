from django import template
from farmer.models import ResponseLog


register = template.Library()

@register.simple_tag
def get_latest_response():
    response = ResponseLog.objects.latest('timestamp')
    return response.content if response else ""
   
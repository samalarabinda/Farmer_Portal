from django import template
from farmer.models import ResponseLog


register = template.Library()

@register.simple_tag
def get_latest_response():
    try:
        response = ResponseLog.objects.latest('timestamp')
        return response.content
    except ResponseLog.DoesNotExist:
        return "Your Meeting link available soon........"
   
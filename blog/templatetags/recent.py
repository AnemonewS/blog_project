from django import template
from blog.models import Similar

register = template.Library()


@register.inclusion_tag("_inc/_recent_widget.html")
def get_recent(recent_class="recent"):
    recent = Similar.objects.all()
    return {"recent": recent, "recent_class": recent_class}

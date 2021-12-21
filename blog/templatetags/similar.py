from django import template
from blog.models import Similar

register = template.Library()


@register.inclusion_tag("Portfolio/similar.html")
def get_similar(similar_class="similar"):
    similar = Similar.objects.all()
    return {"similar": similar, "similar_class": similar_class}
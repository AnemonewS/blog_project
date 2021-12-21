from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag("_inc/_widget.html")
def get_widget(widget_class="widget"):
    categories = Category.objects.all()
    return {"category": categories, "widget_class": widget_class}
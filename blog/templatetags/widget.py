from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag("_inc/_category_widget.html")
def get_widget(widget_class="widget"):
    categories = Category.objects.all()
    return {"categories": categories, "widget_class": widget_class}

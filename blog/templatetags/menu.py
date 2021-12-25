from django import template
from blog.models import Category


register = template.Library()


@register.inclusion_tag("_inc/_menu_navbar.html")
def show_menu(menu_class="menu"):
    categories = Category.objects.all()
    return {"categories": categories, "menu_class": menu_class}


# @register.inclusion_tag("_inc/../templates/blog/_widget.html")
# def show_widget(widget_class = "widget"):
#     categories = Category.objects.all()
#     return {"categories":categories,"widget_class": widget_class}

from django import template
from uenowebsite.models import Category


register = template.Library()
@register.inclusion_tag('uenowebsite/categories.html') 

def get_category_list():
    return {'categories': Category.objects.all()}
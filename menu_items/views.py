from django.shortcuts import render
from .models import MenuItem, Category
import json

def menu(request):
    categories = Category.objects.prefetch_related('menu_items').all()
    sorted_menu = {category.name: category.menu_items.all() for category in categories}
    category_id = request.GET.get('category')
    if category_id:
        menu_items = MenuItem.objects.filter(category_id=category_id)
    else:
        menu_items = MenuItem.objects.all()

    cart = json.loads(request.COOKIES.get('cart', '{}'))

    return render(request, 'menu_reza.html', {
        'sorted_menu': sorted_menu,
        'menu_items': menu_items,
        'categories': categories,
        'cart': cart
    })


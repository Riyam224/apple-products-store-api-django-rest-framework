# Create your views here.
from django.shortcuts import render


def homepage(request):
    apps = [
        {"name": "Cart", "url": "/api/cart/"},
        {"name": "Orders", "url": "/api/orders/"},
        {"name": "Reviews", "url": "/api/reviews/"},
        {"name": "Products", "url": "/api/products/"},
        {"name": "Favorites", "url": "/api/favorites/"},
        {"name": "Users", "url": "/api/users/"},
        {"name": "Core", "url": "/api/core/"},
    ]
    return render(request, "index.html", {"apps": apps})

from django.shortcuts import render
from .models import Product


# design the home view
def homepage(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'site/homepage.html', context)

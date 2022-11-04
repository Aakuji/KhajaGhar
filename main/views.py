from django.shortcuts import render, redirect
from .decorators import user_is_superuser
from products.models import *

# Create your views here. 
def homepage(request):
    products = Product.objects.all().order_by('-id')[:8]
    user = request.user
    # items = Cart.objects.filter(user=user)
    context = {
        'products':products,
    
    }
    return render(request, 'box/home.html',context)
from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def searchResult(request):
    products = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search/search.html', {'query':query,'products':products})

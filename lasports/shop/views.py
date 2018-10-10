from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def home(request):
    return render(request, 'home.html')

#Category View

def allProdCat(request, cat_slug = None):
    cat_page = None
    products_list = None
    if cat_slug != None:
        cat_page = get_object_or_404(Category, slug=cat_slug)
        products_list = Product.objects.filter(category=cat_page, available=True)
    else:
        products_list = Product.objects.all().filter(available=True)
        """ Paginator Code """
    paginator = Paginator(products_list,6)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request, 'shop/category.html', {'category':cat_page, 'products':products})

def ProdCatDetail(request, cat_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=cat_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'shop/product.html', {'product':product})

    

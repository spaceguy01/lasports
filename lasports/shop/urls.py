from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('', views.allProdCat, name="allProdCat"),
    path('<slug:cat_slug>/', views.allProdCat, name="products_by_category"),
    path('<slug:cat_slug>/<slug:product_slug>', views.ProdCatDetail, name="ProdCatDetail"),
]

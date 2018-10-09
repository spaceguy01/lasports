
from django.conf.urls import include
from django.urls import path

from . import views

app_name = 'tutorsitekr'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('subjects', views.subjects, name='subjects'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('pricing', views.pricing, name='pricing'),

]

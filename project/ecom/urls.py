
from django.urls import path, include
from . import views


from .views import products

urlpatterns = [
    path('', views.home, name ="home"),
    path('products/', products.as_view(), name ="products"),
]

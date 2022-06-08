
from django.urls import path, include
from . import views

from .views import products, sellView,productdetailView

urlpatterns = [
    path('', views.home, name ="home"),
    path('products/', products.as_view(), name ="products"),
    path('sell/', sellView.as_view(), name ="sellView"),
    path('product-details/<int:pk>', productdetailView.as_view(), name ="productdetailView"),
] 

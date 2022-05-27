
from django.urls import path, include
from . import views


from .views import products, sellView

urlpatterns = [
    path('', views.home, name ="home"),
    path('products/', products.as_view(), name ="products"),
    path('sell/', sellView.as_view(), name ="sellView"),
]

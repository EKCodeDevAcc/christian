from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<str:product_id>', views.product_detail, name='product_detail')
]

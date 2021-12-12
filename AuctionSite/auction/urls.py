from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns = [
    path('homePage',views.homePage,name='homePage'),
    path('createAuction',views.createAuction,name='createAuction'),
    path('product_details/<int:pk>/',views.product_details, name='product_details'),
]
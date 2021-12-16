from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns = [
    path('homePage',views.homePage,name='homePage'),
    path('createAuction',views.createAuction,name='createAuction'),
    path('productDetails/<int:pk>/',views.productDetails, name='productDetails'),
    path('myPosts',views.myPosts, name='myPosts'),
    path('myProfile/<int:pk>/',views.myProfile, name='myProfile'),
    path('editProduct/<int:pk>/',views.editProduct,name='editProduct'),
    path('editBid/<int:pk>/',views.editBid,name='editBid'),
]
from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns = [
    path('',views.loginPage,name='loginPage'),
    path('registration',views.registration,name='registration'),
    path('homePage',views.homePage,name='homePage'),
    path('logoutUser',views.logoutUser,name='logoutUser'),
]
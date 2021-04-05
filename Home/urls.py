from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('Interior', views.Interior, name='Interior'),
    path('Collection', views.Collection, name='Collection'),
    path('Cleaning', views.Cleaning, name='Cleaning'),
    path('kitchen', views.kitchen, name='kitchen'),
    path('wardrobes', views.wardrobes, name='wardrobes'),
    path('rooms', views.rooms, name='rooms'),
    path('Home_Merchandising', views.Home_Merchandising, name='Home_Merchandising'),
    path('cleaning_kitchen', views.cleaning_kitchen, name='cleaning_kitchen'),
    path('cleaning_bathroom', views.cleaning_bathroom, name='cleaning_bathroom'),
    path('basic_package', views.basic_package, name='basic_package'),
    path('testing', views.testing, name='testing'),
    path('Contact', views.Contact, name='Contact'),
    path('Repair', views.Repair, name='Repair'),
    path('homecleaning', views.homecleaning, name='homecleaning'),
    path('proj_delivered', views.proj_delivered, name='proj_delivered'),
    path('howitworks', views.howitworks, name='howitworks'),
    path('faqs', views.faqs, name='faqs'),
    path('refrigerator', views.refrigerator, name='refrigerator'),
    path('chimney', views.chimney, name='chimney'),
    path('mwave', views.mwave, name='mwave'),
    path('onebhk', views.onebhk, name='onebhk'),









    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('signup', views.handleSignup, name='handleSignup'),

    ]

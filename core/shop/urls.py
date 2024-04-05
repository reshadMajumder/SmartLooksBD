from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path ('' , home, name='home' ),
    path ('man/' , man, name='man' ),
    path ('women/' , women, name='women' ),
    path ('accessories/' , accessories, name='accessories' ),
    path ('others/' , others, name='others' ),
    path ('cart/' , cart, name='cart' ),
    path ('product-details/cart/' , cart, name='cart' ),
    path ('product-details/<int:id>/' , productDetails, name='productDetails' ),
    path ('login/' , login, name='login' ),
    path ('register/' , register, name='register' ),
    path('logout/',handlelogout,name='logout'),
    path('privacy/',privacy,name='privacy'),

    path ('checkout/' , checkOut, name='checkOut' ),
    path ('checkoutMassage' , checkOutMsg, name='checkOutMsg' ),

]

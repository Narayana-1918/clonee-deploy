"""
URL configuration for clonee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userregister/',userregister,name='userregister'),
    path('userlogin/',userlogin,name='userlogin'),
    path('',home,name='home'),
    path('hotel_list/',hotel_list,name='hotel_list'),
    path('user_profile/',profile,name='user_profile'),
    path('menu_list/<int:id>',menu_list,name='menu_list'),
    path('view_cart/',view_cart,name='view_cart'),
    path('addetail/',addetail,name='addetail'),
    # path('buy_now/<int:id>',buy_now,name='buy_now'),
    # path('create_order/',create_order,name='create_order'),
    path('remove_from_cart/<int:id>',remove_from_cart,name='remove_from_cart'),
    path('delete_item/<int:id>',delete_item,name='delete_item'),
    path('add_to_cart/<int:id>',add_to_cart,name='add_to_cart'),

    path('userlogout/',userlogout,name='userlogout'),
    path('search_view/',search_view,name='searchview'),
    path('menu_search/',menu_search,name='menu_search'),
    path('success/',success,name='success'),






    path('create/', create_order, name='create_order'),
    path('order/<int:order_id>/', order_detail, name='order_detail'),



    ]

   



if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
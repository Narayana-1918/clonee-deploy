from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *
# Register your models here.
@register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display=['restaurant_id','restaurant_name','restaurant_description','restaurant_address','restaurant_phone','restaurant_image',]

@register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display=['menu_id','restaurant','item_name','item_price']
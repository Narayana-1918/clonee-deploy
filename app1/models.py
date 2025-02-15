from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    restaurant_id=models.IntegerField(primary_key=True)
    restaurant_name=models.CharField(max_length=30)
    restaurant_description=models.CharField(max_length=40)
    restaurant_address=models.CharField(max_length=50)
    restaurant_phone=models.CharField(max_length=40)
    restaurant_image=models.ImageField(upload_to='restaurant_images/')
    restaurant_rating=models.FloatField()
    # restaurant_delivery_time=models.IntegerField()
    restaurant_delivery_charge=models.FloatField()
    restaurant_cusine=models.CharField(max_length=25)
    restaurant_is_open=models.BooleanField(default=True)
    

    def __str__(self):
       return self.restaurant_name

class Menu(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    item_description = models.TextField()
    item_price = models.FloatField()
    item_image = models.ImageField(upload_to='menu_images/')
    item_category = models.CharField(max_length=50)
    item_is_available = models.BooleanField(default=True)


    def __str__(self):
        return self.item_name
    

class New_user(User):
    phone_no=models.CharField(max_length=21)
    address=models.CharField(max_length=40)

    def __str__(self):
        return self.username
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


class Cart_items(models.Model):
    menu=models.ForeignKey(Menu,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity}x{self.menu.item_name}'

class Delivery_details(models.Model):
    country=models.CharField(max_length=25)
    full_name=models.CharField(max_length=35)
    mobile_number=models.IntegerField()
    landmark=models.CharField(max_length=25)
    pincode=models.IntegerField()
    default_address=models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.full_name},{self.mobile_number}'
from django.db import models
import datetime
from  django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create Customer Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # One profile with One user (one - one)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)
    
    
    def __str__(self):
        return self.user.username

# create a user profile by default when user signs up

#When a new user signs up:
'''The User model (the sender) triggers a post_save signal.
The create_profile function is called with:
The user instance (the specific user who signed up) as instance.
A boolean (created) that tells whether it's a new user.
Any additional arguments captured in **kwargs (though not used here).'''

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

# Automate the profile thing
post_save.connect(create_profile, sender=User)     #This line connects the create_profile function to a signal called post_save, which is triggered after a User instance is saved. It means that every time a User is created, the create_profile function will be called automatically.


# Categories of Products
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

# customers
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



# All of our Products
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default="", blank= True, null= True)
    image =models.ImageField(upload_to='uploads/product/')

    #Add sale stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.IntegerField(default=0, blank=True, null=True)


    def __str__(self):
        return self.name

#Customer Orders
class Order(models.Model):
    Product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    customer =  models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity =  models.IntegerField(default=1)
    address = models.CharField(max_length=100,default='',blank=True)
    phone = models.CharField(max_length=20,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.Product


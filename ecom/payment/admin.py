from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem
# Register your models on the admin section.

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


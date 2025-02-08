from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User
# Register your models on the admin section.

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


# Create an orderItem Inline
class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0

# Extend Our Order Model
class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields =['date_ordered']
    fields = ["user","full_name","email","Shipping_Address","amount_paid","date_ordered","shipped"]
    inlines = [OrderItemInline]

# Unregister the Order Model

admin.site.unregister(Order)

# Re-Register our Order And OrderAdmin
admin.site.register(Order, OrderAdmin)


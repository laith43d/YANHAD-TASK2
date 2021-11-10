from django.contrib import admin

# Register your models here.
from commerce.models import Product, Order, Item, OrderStatus, Category, Merchant, ProductImage, Label, Vendor, City, \
    Address

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(OrderStatus)
admin.site.register(Category)
admin.site.register(Merchant)
admin.site.register(ProductImage)
admin.site.register(Label)
admin.site.register(Vendor)
admin.site.register(City)
admin.site.register(Address)

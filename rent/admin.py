from django.contrib import admin
from .models import Type, Size, Vehicle, Customer, Rental, Rate

admin.site.register(Vehicle)
admin.site.register(Type)
admin.site.register(Size)
admin.site.register(Customer)
admin.site.register(Rental)
admin.site.register(Rate)

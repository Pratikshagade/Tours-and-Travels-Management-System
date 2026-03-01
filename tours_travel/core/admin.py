from django.contrib import admin
from .models import Package, Address

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'destination', 'price']
    filter_horizontal = ['hotels', 'foods']  # ✅ makes selection easier

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'city', 'state', 'country', 'hotel', 'user']
    search_fields = ['city', 'state', 'country']    

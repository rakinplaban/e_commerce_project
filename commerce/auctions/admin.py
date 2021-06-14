from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import User,auction_listing
# Register your models here.

class auction_listing_admin(admin.ModelAdmin):
    list_display = ("id","title","author","category","starting_bid")


admin.site.register(User,)
admin.site.register(auction_listing,auction_listing_admin)
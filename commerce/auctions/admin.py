from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import User,auction_listing,bids,comment
# Register your models here.

class auction_listing_admin(admin.ModelAdmin):
    list_display = ("id","title","author","creating_date","category","starting_bid","status")

class bid_listing(admin.ModelAdmin):
    list_display = ("id","user","auction","bid")

class comment_list(admin.ModelAdmin):
    list_display = ("id","post","author","date","content")

admin.site.register(User,)
admin.site.register(auction_listing,auction_listing_admin)
admin.site.register(bids,bid_listing)
admin.site.register(comment,comment_list)
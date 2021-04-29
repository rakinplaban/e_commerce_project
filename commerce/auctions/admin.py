from django.contrib import admin
from .models import User,auction_listing
# Register your models here.

admin.site.register(User,)
admin.site.register(auction_listing,)
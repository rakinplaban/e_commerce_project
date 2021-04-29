from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class auction_listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    starting_bid = models.IntegerField()
    category = models.CharField(max_length=120)
    img = models.URLField()

    def __str__(self):
        return f"Title {title} : Category {category} Starting price {starting_bid}"
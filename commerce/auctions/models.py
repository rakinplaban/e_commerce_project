from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE


class User(AbstractUser):
    pass

class auction_listing(models.Model):
    author = models.ForeignKey(User,default=1,on_delete=CASCADE)
    creating_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    starting_bid = models.IntegerField()
    category = models.CharField(max_length=120)
    img = models.URLField()

    def __str__(self):
        return f"{self.id} : {self.title}  Category {self.category} Starting price {self.starting_bid}"



    
    
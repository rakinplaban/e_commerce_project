from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator


class User(AbstractUser):
    pass

class auction_listing(models.Model):
    author = models.ForeignKey(User,default=1,on_delete=CASCADE)
    creating_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    starting_bid = models.FloatField()
    category = models.CharField(max_length=120)
    img = models.URLField()
    favourite = models.ManyToManyField(User,blank=True,related_name="favourite")
    status = models.BooleanField(default=True)
    #newmanager = NewManager()

    def __str__(self):
        return f"{self.id} : {self.title}  Category {self.category} Starting price {self.starting_bid}"

class bids(models.Model):
    auction = models.ForeignKey(auction_listing,on_delete=CASCADE)
    user = models.ForeignKey(User,on_delete=CASCADE)
    bid = models.FloatField(validators=[MinValueValidator(0.01)])

    def __str__(self):
        return f"{self.bid}"


class comment(models.Model):
    author = models.ForeignKey(User,on_delete=CASCADE,related_name="commenter")
    post = models.ForeignKey(auction_listing,related_name="Comments",on_delete=CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        #try:
        return f"{self.content}"
        #except author.RelatedObjectDoesNotExist:
        #    return f"{self.post.title} : {self.content}"


 
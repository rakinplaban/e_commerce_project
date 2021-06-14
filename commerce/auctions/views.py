from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User,auction_listing


def index(request):
    return render(request, "auctions/index.html",{
        'listing' : auction_listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):  
    if request.method == "POST":
        if request.user.is_authenticated:
            author = request.session.user
            title = request.POST["title"]
            description = request.POST["description"]
            starting_bid = request.POST["starting_bid"]
            category = request.POST["category"]
            image_link = request.POST["image_link"]

            create_listingdata = auction_listing(title = title,description = description,starting_bid = starting_bid,
                category = category,img = image_link)
            create_listingdata.save()

            return render(request,"auctions/mylist.html",{
                "author" : author,
                "title" : title,
                "description" : description,
                "starting_bid" : starting_bid,
                "category" : category,
                "image_link"  : image_link
            })
    return render(request, "auctions/createlisting.html")


def display_list(request,list_id):
    listing = auction_listing.objects.get(pk=list_id)
    return render(request,"auctions/list.html",{
        "list" : listing
    })

def categories(request):
    listee = auction_listing.objects.all()
    liste = listee.order_by('category').values('category').distinct()
    return render(request,"auctions/categories.html",{
        "category" : liste
    })

def displaycat(request,category):
    listee = auction_listing.objects.filter(category=category)
    return render(request,"auctions/index.html",{
        "listing" : listee
    })
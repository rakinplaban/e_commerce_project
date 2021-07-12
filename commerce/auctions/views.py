from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import User, auction_listing, bids, comment
from .forms import comment_form, bid_form
from datetime import datetime
from django.core.exceptions import ValidationError
from django.contrib import messages


def index(request):
    return render(request, "auctions/index.html",{
        'listing' : auction_listing.objects.filter(status=True)
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
            author = request.user
            creating_date = datetime.now()
            title = request.POST["title"]
            description = request.POST["description"]
            starting_bid = request.POST["starting_bid"]
            category = request.POST["category"]
            image_link = request.POST["image_link"]

            create_listingdata = auction_listing(title = title,author = author,creating_date=creating_date ,description = description,starting_bid = starting_bid,
                category = category,img = image_link)
            create_listingdata.save()
            return render(request,"auctions/mylist.html",{
                "title" : title,
                "author" : author,
                "creating_date" : creating_date,
                "description" : description,
                "starting_bid" : starting_bid,
                "category" : category,
                "image_link"  : image_link
            })
    return render(request, "auctions/createlisting.html")
'''
def biding(request,bid):
    if request.method == "POST":
        auction = request.POST["auction"]
        bid = request.POST["bid"]
        if bid <= auction.starting_bid:
            return render(request,"auctions/list.html",{
                "message" : "Bid must be greater then starting bid."})
        else:
            bids = bids(auction = auction,bid = bid)
            bids.save()
        return render(request,"auctions/list.html",{
            "auction" : auction,
            "bid" : bid
        })
'''
'''
def comment(request,id):
    if request.method == "POST":
        user = request.user
        post = get_object_or_404(auction_listing,pk=id)
        date = datetime.now()
        content = comment_form(request.POST)
        content.save()
        comments = comments(user=user,post=post,date=date,content=content)
        return render(request,"auctions/list.html",{
            "user" : user,
            "post" : post,
            "date" : date,
            "content" : content
        })
    return render(request,"auctions/list.html",{
        "form" : comment_form()
    })
'''       

def display_list(request,list_id):
    listing = auction_listing.objects.get(pk=list_id)

    fav = False

    if listing.favourite.filter(id=request.user.id).exists():
        fav = True
    mini_error = False
    status = True
    if listing.status is False:
        status = False

    if request.method == "POST":
        
        if request.user.is_authenticated:
            form = comment_form(request.POST)
            bform = bid_form(request.POST)
            author = request.user
            date = datetime.now()
            post = listing
            user = request.user
            #auction = listing
            if form.is_valid():
                content = form.save(commit = False)
                commentdata = comment(author = author,date=date,post=post,content=content)
                commentdata.save()

            if bform.is_valid():
                instance = bform.save(commit=False)
                instance.user = user
                instance.auction = post
                if (float(instance.bid) > post.starting_bid) and (float(instance.bid)> post.current_price):
                    instance.save()
                    listing.current_price = instance.bid
                    listing.save()
                    messages.success(request,"Congratulations! Your bid has been accepted. 😊")
                else:
                    #raise ValidationError("Please insert amount greater than starting bid and current price.")
                    messages.error(request,"Sorry! Please insert amount more then current price & starting bid.")
                #biddata = bids(user=user,auction=post,bid=instance)
                #biddata.save()

                
            return HttpResponseRedirect(reverse("displaylistitem",kwargs={"list_id" : list_id}))
           

        else:
            return render(request,"auctions/list.html",{
                "message" : "Please log in for comment!"
            })
    else:
        form = comment_form()
        bform = bid_form()

    return render(request,"auctions/list.html",{
        "list" : listing,
        "form" : form,
        "bform" : bform,
        "fav" : fav,
        "status" : status,
        "ValidationError" : ValidationError
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


def status(request,list_id):
    listing = get_object_or_404(auction_listing,id = list_id)
    
    if listing.status is True:
        listing.status = False
        listing.save()
    else:
        listing.status = True
        listing.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def favourite(request,id):
    listing = get_object_or_404(auction_listing,id=id)
    if listing.favourite.filter(id = request.user.id).exists():
        listing.favourite.remove(request.user)
    else:
        listing.favourite.add(request.user)
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def watchlist(request):
    listing = auction_listing.objects.filter(favourite=request.user)
    return render(request,"auctions/watchlist.html",{
        "listing" : listing
    })

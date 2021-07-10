from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.create_listing, name="createlisting"),
    path("mylist", views.create_listing, name="mylist"),
    path("<int:list_id>",views.display_list,name="displaylistitem"),
    path("status/<int:list_id>", views.status,name="status"),
    path("fav/<int:id>",views.favourite,name="favourite"),
    path("watchlist",views.watchlist,name="watchlist"),
    path("categorise",views.categories,name="categories"),
    path("<str:category>",views.displaycat,name="displaycat"),
]

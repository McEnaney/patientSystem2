from django.urls import path
from . import views

# creates URLs for the site
urlpatterns = [
    path("", views.home, name="home")
]
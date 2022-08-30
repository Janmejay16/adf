from django.urls import path

#imported views
from . import views

urlpatterns = [
    path("", views.index, name="Home Page"),
    path("custom/", views.custom, name="Custom Page")
]

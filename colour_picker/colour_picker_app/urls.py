from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="colour-picker-main"),
    path("request-colour/", views.request_colour, name="colour-picker-request"),
]

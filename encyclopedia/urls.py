from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("newentry", views.new_entry, name="newentry"),
    path("randompage", views.random, name="randompage"),
    path("error", views.entry, name="error"),
    path("already_exists_error", views.new_entry, name="already_exists_error"),
    path("<str:title>", views.entry, name="entry")
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list/", views.dblist, name="list"),
    path("create/", views.create, name="create"),
    path("delete/", views.delete, name="delete"),
]

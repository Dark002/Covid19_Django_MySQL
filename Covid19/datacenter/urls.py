from django.urls import path
from . import views


app_name="datacenter"
urlpatterns = [
    path("", views.home,name="home"),
]
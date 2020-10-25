from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="hello"),
    path("data",views.get_data,name="get_data")
]

from django.urls import path, include
from .views import*
from . import views

urlpatterns = [
    path("",home, name="home"),
    path("signup/", authView, name="authView"),
    path("", include("django.contrib.auth.urls")),
    
]




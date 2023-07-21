from django.urls import path
from . import views

# URLConf module = URL configuration
urlpatterns = [
    path('hello/', views.say_hello), # Always end routes with a forward slash "hello/"
]
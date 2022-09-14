from django.urls import path
from . import views

# URL Conf module
urlpatterns = [
    path('hello/', views.say_hello),
    path('hello/<name>/', views.say_hello_to),
]

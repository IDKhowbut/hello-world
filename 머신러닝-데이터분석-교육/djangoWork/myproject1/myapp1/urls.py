from django.urls import path
from myapp1 import views

urlpatterns = [
    path('', views.index),
]

#http://127.0.0.1:8000/myapp1
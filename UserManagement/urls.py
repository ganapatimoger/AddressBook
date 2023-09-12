from django.contrib import admin
from django.urls import path
from .views.users import UserViewset

urlpatterns = [
    # path('user/', users),
     path('user/', UserViewset.as_view(), name="register"),
]

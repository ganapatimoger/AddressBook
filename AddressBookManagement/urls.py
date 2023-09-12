from django.urls import path, include
from .views.address import AddressBookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('address', AddressBookViewSet, basename='address')

urlpatterns = [
    path('', include(router.urls)),
]
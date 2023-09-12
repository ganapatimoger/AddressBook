from django.db import models
from UserManagement.models import User


class AddressBook(models.Model) :
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    pincode = models.CharField(max_length=10)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='address_list')

    def __str__(self):
        return self.street

    class Meta:
        db_table = 'address'
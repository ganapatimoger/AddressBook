from rest_framework import serializers
from ..models import AddressBook
import re


class AddressBookSerializer(serializers.ModelSerializer) :
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = AddressBook
        fields = ['id', 'street', 'city','latitude', 'longitude', 'pincode']

    def validate_latitude(self, value):
        """Validating the latitude value"""
        if value is not None and (value < -90 or value > 90):
            raise serializers.ValidationError("Latitude must be between -90 and 90 degrees.")
        return value

    def validate_longitude(self, value):
        """Validaing the longitude value"""
        if value is not None and (value < -180 or value > 180):
            raise serializers.ValidationError("Longitude must be between -180 and 180 degrees.")
        return value

    def validate_pincode(self, value):
        """Validation for pincode """
        # Example: You can use regular expressions or other validation logic here
        if not value or not re.match(r'^[0-9]{5}$', value):
            raise serializers.ValidationError("Invalid postal code format. It should be a 5-digit number.")
        return value

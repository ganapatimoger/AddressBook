from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from ..models import User
import re
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    phone = serializers.CharField(
        validators = [UniqueValidator(queryset=User.objects.all())]
    )
    class Meta:
        model = User
        fields = ['password', 'first_name', 'last_name', 'email', 'phone']

    def validate_password(self, value):
        # Hash the password before saving it to the database
        return make_password(value)


    def validate_phone_number(self, value):
        pattern = r'^\+?[0-9]+$'  # Allows digits and an optional leading '+'

        if not re.match(pattern, value):
            raise serializers.ValidationError("Invalid phone number format. It should contain only digits and an optional leading '+'.")

        return value
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class User(AbstractBaseUser):
    """
    Creating User model and table
    """
    username = None
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25, null=True)
    email = models.EmailField(max_length=50, null=True, unique=True)
    phone = models.CharField(max_length=20, unique=True)

    USERNAME_FIELD = 'email'

    objects = BaseUserManager()

    def __str__(self):
        return self.first_name
    class Meta:
        db_table = 'users'
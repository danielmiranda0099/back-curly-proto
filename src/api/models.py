from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone

from .manager import CustomUserManager


class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255,unique=True,)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=25)
    adress = models.CharField(max_length=255)
    id_card = models.CharField(max_length=20)
    date_joined = models.DateTimeField(default=timezone.now)

    is_active = models.BooleanField(default=True)
    is_client = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('name',)

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

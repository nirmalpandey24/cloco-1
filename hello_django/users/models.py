from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    eid = models.IntegerField(_("employee ID"), null=True, blank=True)
    ename = models.CharField(_("employee name"), max_length=50, blank=True)
    esalary = models.FloatField(_("employee salary"), default=0.0)
    password=None

    # Add a default username, you can change it to whatever default you prefer
    username = models.CharField(_("username"), max_length=150, unique=True, default='user')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

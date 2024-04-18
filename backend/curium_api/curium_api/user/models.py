from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid

class MyAccountManager(BaseUserManager):
    def create_user(self, email_id, fname, lname, role, password=None):
        if not email_id:
            raise ValueError("Users must have an email address")

        user = self.model(
            email_id=self.normalize_email(email_id), fname=fname, lname=lname, role=role
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    ROLE_CHOICES = (
        ('Normal User', 'Normal User'),
        ('Surgeon', 'Surgeon'),
        ('Teleradiologist', 'Teleradiologist'),
        ('Radiologist', 'Radiologist'),
    )

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email_id = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Normal User')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email_id", "role"]

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_module_perms(self, app_label):
        return True

from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.common.models import BaseModel


class Account(BaseModel, AbstractUser):
    class AuthStatus(models.TextChoices):
        FIRST_STEP = 'first step'
        SECOND_STEP = 'second step'
        THIRD_STEP = 'third step'

    auth_step = models.CharField(max_length=15, choices=AuthStatus.choices, default=AuthStatus.FIRST_STEP)

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

    def check_email(self):
        if self.email:
            normalize_email = self.email.lower()
            self.email = normalize_email

    def save(self, *args, **kwargs):
        self.check_email()
        super(Account, self).save(*args, **kwargs)

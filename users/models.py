from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from random import choice
from datetime import timedelta


class ConfirmationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_code(self):
        self.code = ''.join(choice('0123456789') for _ in range(6))

    def is_expired(self):
        return timezone.now() - self.created_at > timedelta(minutes=5)





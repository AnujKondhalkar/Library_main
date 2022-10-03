from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    class Meta:

        fields = ['username']

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()           # To run same parrent method which already exist

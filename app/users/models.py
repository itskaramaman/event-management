from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile model with one to one relationship to yser
    """
    image = models.ImageField(upload_to='profile_images/', default='default.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} profile'

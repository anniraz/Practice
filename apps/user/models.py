from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    avatar = models.ImageField(
        upload_to='images',
        blank=True,
        null=True
    )
    last_action=models.DateTimeField(default=timezone.now)
    email=models.EmailField(null=True,blank=True)
    REQUIRED_FIELDS=['email']


    def __str__(self):
        return f' {self.username}'
    


class Visits(models.Model):
    
    count = models.IntegerField(default=0)
    day=models.DateField(auto_now_add=True)
    all_count=models.IntegerField(default=0)

    def __str__(self):
        return f'id :{self.id}  date: {self.day} visits: {self.count} '


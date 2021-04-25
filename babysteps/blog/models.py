from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # podria ser auto_now=True
    author = models.ForeignKey(User, on_delete=models.CASCADE) # si se elimina el usuario, se elimina el posteo

    def __str__(self):
        return self.title
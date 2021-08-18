# Create your models here.

from enum import unique
from django.db import models
from django.contrib.auth.models import User

class Film(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    

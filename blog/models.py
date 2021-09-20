from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):

    nickname = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)
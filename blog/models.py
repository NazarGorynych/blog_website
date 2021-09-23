from django.db import models
# from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):

    nickname = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)


class Post(models.Model):

    published_date = models.DateField()
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # slug = models.SlugField(unique=True)
    # text = models.CharField(max_length=300)
    # image = models.ImageField(upload_to='images')
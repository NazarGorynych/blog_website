from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

    # def __str__(self):
    #     return f'{self.username} - {self.email}'


class Post(models.Model):

    published_date = models.DateField()
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.title}'


    # image = models.ImageField(upload_to='images')
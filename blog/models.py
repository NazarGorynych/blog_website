from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class UserFollowing(models.Model):
    user_id = models.ForeignKey("User", related_name="following", on_delete=models.CASCADE)
    following_user_id = models.ForeignKey("User", related_name="followers", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Post(models.Model):

    published_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog')
    text = models.TextField()

    def __str__(self):
        return f'{self.title}'


    # image = models.ImageField(upload_to='images')
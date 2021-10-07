from django.db import models


class User(models.Model):

    nickname = models.CharField(max_length=30, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.nickname} - {self.email}'


class Post(models.Model):

    published_date = models.DateField()
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.title}'


    # image = models.ImageField(upload_to='images')
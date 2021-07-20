from django.db import models

# Create your models here.


class UserModel(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

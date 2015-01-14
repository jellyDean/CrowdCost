from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Users(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

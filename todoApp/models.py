from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10, verbose_name="name")
    pw = models.CharField(max_length=15, verbose_name="password")

from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=128,null=True)
    last_name = models.CharField(max_length=128, null=True)
    email = models.EmailField(max_length=264, unique=True)
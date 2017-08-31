from django.db import models

# Create your models here.
class User(models.Model):
    """docstring for Users."""
    firstname = models.CharField(max_length=50, unique=True)
    lastname = models.CharField(max_length=50, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.lastname

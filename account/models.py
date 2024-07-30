from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

class LearnerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=2)
    date_of_birth = models.CharField(max_length=10)
    account_type = models.CharField(max_length=10)
    profile = models.ImageField(upload_to="images/profile/", blank=True)


    def __str__(self):
        return self.email




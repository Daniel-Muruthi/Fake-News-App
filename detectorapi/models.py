from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class News(models.Model):
  text = models.TextField()

class Contact(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = PhoneNumberField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.username
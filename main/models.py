from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Userdetail(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^/d{10}$',message = 'The Phone number is not correct')
    phone = models.CharField(max_length=10,validators=[phone_regex])
    Query = models.TextField()
    Query_date = models.DateTimeField()
    

from django.db import models

# Create your models here.
class ViewBooks(models.Model):

    BookName= models.CharField( max_length=200)
    author= models.CharField( max_length=100)
    publisher= models.models.CharField( max_length=100)
    price= models.IntegerField()
    image=models.FileField()
    new= models.BooleanField()
    userid=models.CharField( max_length=50)
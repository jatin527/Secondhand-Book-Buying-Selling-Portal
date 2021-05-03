from django.db import models


# Create your models here.


class ViewBooks(models.Model):

    BookName = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    category = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.FileField(upload_to="booksImage")
    new = models.BooleanField()
    userid = models.CharField(max_length=50)
    purchasedate = models.DateField(auto_now=False, auto_now_add=False)
    audio = models.FileField(null=True, upload_to="audio")
    upload_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=50)


class Cart(models.Model):

    id_book = models.IntegerField()
    id_user = models.IntegerField()


class Orders(models.Model):

    id_book = models.IntegerField()
    id_user = models.IntegerField()
    status = models.CharField(max_length=100)
    purchasedate = models.DateField(auto_now=True)

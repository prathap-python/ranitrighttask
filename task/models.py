from django.db import models
class Details(models.Model):
    Name=models.CharField(max_length=256)
    Url=models.CharField(max_length=256)
    Phonenumber=models.IntegerField()
class Search(models.Model):
    SearchedName=models.CharField(max_length=256)
class GetImages(models.Model):
    EnteredLink=models.CharField(max_length=256)


# Create your models here.

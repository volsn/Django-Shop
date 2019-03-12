from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=124, unique=True)
    description = models.CharField(max_length=512)


class Product(models.Model):
    title = models.CharField(max_length=124, unique=True)
    price = models.IntegerField()
    short_description = models.CharField(max_length=256)
    description = models.TextField()
    category = models.ManyToManyField(Category)

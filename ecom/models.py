import datetime
import uuid
from django.db import models
from django.utils.timezone import now
# Create your models here.


def getpath(obj, filename):
    return "uploads/%s.%s" % (str(uuid.uuid4()).replace("-", ""), filename.split(".")[-1])


class Product(models.Model):
    class Meta:
        db_table = "Product"
    category = models.CharField(max_length=45, default='Product')
    brand = models.CharField(max_length=15, null=False, blank=True)
    model = models.CharField(max_length=15, blank=True)
    razmer = models.CharField(max_length=10, blank=True)
    price = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to=getpath)


class Shoe(models.Model):
    class Meta:
        db_table = "Shoe"
    category = models.CharField(max_length=45, default='Shoe')
    brand = models.CharField(max_length=15, null=False, blank=True)
    model = models.CharField(max_length=15, blank=True)
    razmer = models.CharField(max_length=10, blank=True)
    price = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to=getpath)


class Dress(models.Model):
    class Meta:
        db_table = "Dress"
    category = models.CharField(max_length=45, default='Dress')
    brand = models.CharField(max_length=15, null=False, blank=True)
    model = models.CharField(max_length=15, blank=True)
    razmer = models.CharField(max_length=10, blank=True)
    price = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to=getpath)


class Bag(models.Model):
    class Meta:
        db_table = "Bag"
    category = models.CharField(max_length=45, default='Bag')
    brand = models.CharField(max_length=15, null=False, blank=True)
    model = models.CharField(max_length=15, blank=True)
    color = models.CharField(max_length=10, blank=True)
    price = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to=getpath)


class Treasure(models.Model):
    class Meta:
        db_table = "Treasure"
    category = models.CharField(max_length=45, default='Treasure')
    brand = models.CharField(max_length=15, null=False, blank=True)
    model = models.CharField(max_length=15, blank=True)
    razmer = models.CharField(max_length=10, blank=True)
    price = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to=getpath)


class Hijab(models.Model):
    class Meta:
        db_table = "Hijab"
    category = models.CharField(max_length=45, default='Hijab')
    brand = models.CharField(max_length=15, null=False, blank=True)
    model = models.CharField(max_length=15, blank=True)
    razmer = models.CharField(max_length=10, blank=True)
    price = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to=getpath)


class Romol(models.Model):
    class Meta:
        db_table = "Romol"
    category = models.CharField(max_length=45, default='Romol')
    brand = models.CharField(max_length=15, null=False, blank=True)
    made = models.CharField(max_length=15, blank=True)
    material = models.CharField(max_length=10, blank=True)
    price = models.CharField(max_length=15, blank=True)
    image = models.ImageField(upload_to=getpath)


class User(models.Model):
    first_name = models.CharField(max_length=35)
    phone = models.CharField(max_length=15)
    response = models.BooleanField(default=False)
    date = models.DateTimeField(default=now)
    product_id = models.CharField(max_length=35, default="no")

    class Meta:
        db_table = 'Customer'

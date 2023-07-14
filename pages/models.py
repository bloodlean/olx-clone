from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product/%Y/%m/%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Transport(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='transport/%Y/%m/%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Furniture(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='transport/%Y/%m/%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Cloth(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='transport/%Y/%m/%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Sport(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='transport/%Y/%m/%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title
from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.name


from django.db import models
from cloudinary.models import CloudinaryField


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="FoodItems/", blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField(folder="Gana")

    def __str__(self):
        return self.name
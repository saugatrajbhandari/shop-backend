from enum import unique
from itertools import product
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
import uuid


class Product(models.Model):
    _id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=225, null=True, blank=True)
    image = models.ImageField(upload_to="products", null=True, blank=True)
    brand = models.CharField(max_length=225, null=True, blank=True)
    category= models.ForeignKey("Category", on_delete=models.SET_NULL, related_name='product',  blank=True, null=True)
    price= models.IntegerField(null=True, blank=True)
    description= models.TextField(null=True, blank=True)
    countInStock= models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    @property
    def numOfReview(self):
        return self.review.count()

    def __str__(self):
        return f"{self.name}-{self._id}"


class Review(models.Model):
    _id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="review")
    review = models.TextField(null=True, blank=True)
    rating= models.PositiveIntegerField(default=4,
    validators=[MaxValueValidator(5), MinValueValidator(1)], null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name}-{self.user.username}-{self._id}-review"


class Category(models.Model):
    _id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    category = models.CharField(max_length=225, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category



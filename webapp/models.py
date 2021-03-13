from django.db import models

# Create your models here.
class Product(models.Model):
    # a list of columns from products.json
    title = models.CharField(max_length=200)
    isbn13 = models.CharField(max_length=20, null=True, blank=True)
    isbn = models.CharField(max_length=20, null=True, blank=True)
    image = models.CharField(max_length=200)
    product_id = models.CharField(max_length=20)
    link = models.CharField(max_length=200)
    customer_rating = models.FloatField(null=True)

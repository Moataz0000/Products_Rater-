from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
from django.utils.text import slugify


"""
any model you have, no pushing the ID with your endpoints, use 'uuid'   ---> Important
"""


class Category(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=250)
    creation_date = models.DateField(auto_now=True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kewargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kewargs)    


class Product(models.Model):
    uuid  = models.UUIDField(default=uuid.uuid4, editable=False , unique=True)
    name  = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField(max_length=1000)
    creation_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ['-creation_date']


    def __str__(self):
        return self.name





class Rating(models.Model):
    uuid  = models.UUIDField(default=uuid.uuid4, editable=False , unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    stars   = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) 


    class Meta:
        unique_together = (('user', 'product')) # user not allow to rate the one of product twics
        index_together  = (('user', 'product'))


    def __str__(self):
        return f'{self.product}'








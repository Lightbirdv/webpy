from django.db import models

# Create your models here.
from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Clothing(models.Model):
    SIZE = [
        ('XS', 'very small'),
        ('S', 'small'),
        ('M', 'medium'),
        ('L', 'large'),
        ('XL', 'extra large'),
        ('XXL', 'extra extra large')
    ]

    TYPE = [
        ('Jackets','jackets'),
        ('T-Shirts','t-shirts'),
        ('Shirts', 'shirts'),
        ('Pants', 'pants'),
        ('Jeans', 'jeans'),
        ('Pullovers', 'pullovers'),
        ('Hoodies', 'hoodies'),
        ('Shoes', 'shoes'),
        ('Basics', 'basics'),
        ('Accessoires', 'accessoires'),
        ('Underwear', 'underwear'),
        ('Dresses', 'dresses'),
        ('Suits', 'suits'),
    ]

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    collection = models.CharField(max_length=50)
    size = models.CharField(max_length=3,
                            choices=SIZE,
                            )

    type = models.CharField(max_length=12,
                            choices=TYPE,
                            )

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='users',
                             related_query_name='user',
                             )

    class Meta: 
        ordering = ['name', '-type']
        verbose_name = 'Clothing'
        verbose_name_plural = 'Clothes'

    def __str__(self):
        return self.name + ' (' + self.collection + ')'

    def __repr__(self):
        return self.name + ' / ' + self.description + ' / ' + self.color + ' / ' + self.collection + ' / ' + self.size + ' / ' + self.type
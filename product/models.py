from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    title = models.CharField('название', max_length=30)

    def __str__(self):
        return self.title


class Product(models.Model):
    COUNTRY = (
        ('RU', 'Россия'),
        ('KZ', 'Казахстан')
    )
    title = models.CharField('название', max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    author = models.ManyToManyField(User)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField()
    country = models.CharField(max_length=30, choices=COUNTRY)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.category}'
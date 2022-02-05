from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    slug = models.SlugField()
    image = models.ImageField(upload_to='products')
    thumbnail = models.ImageField(upload_to='thumbnails')

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey()

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

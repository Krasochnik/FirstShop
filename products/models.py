from django.db import models

# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, blank=True, null=True
    )
    name = models.CharField(
        verbose_name='name', max_length=64
    )
    description = models.TextField(
        verbose_name='description'
    )
    price = models.DecimalField(
        verbose_name='price', decimal_places=2, max_digits=10
    )
    publish_date = models.DateTimeField(
        auto_now_add=True, verbose_name='publish_date'
    )

    def __str__(self):
        return f'{self.name}'

class Feedback(models.Model):
    Product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='feedback'
    )
    text = models.TextField(
        verbose_name='text'
    )
    publish_date = models.DateTimeField(
        auto_now_add=True, verbose_name='publish_date'
    )
    author = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE
    )
    rating = models.IntegerField(
        default=1, verbose_name='rating'
    )

    def __str__(self):
        return f'{self.text}'

class Category(models.Model):
    text = models.CharField(
        max_length=48, verbose_name='Text'
    )

    def __str__(self):
        return f'{self.text}'
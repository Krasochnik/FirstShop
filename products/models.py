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
        verbose_name='описание'
    )
    price = models.DecimalField(
        verbose_name='цена', decimal_places=2, max_digits=10, default=0.00
    )
    publish_date = models.DateTimeField(
        auto_now_add=True, verbose_name='publish_date'
    )
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    image=models.ImageField(
        upload_to="products_images",blank=True, null=True, verbose_name="изображение"
    )
    discount= models.DecimalField(
        decimal_places=2, max_digits=10, default=0.00, verbose_name='Скидка в %'
    )
    quantity=models.PositiveIntegerField(
        default=0,  verbose_name="количество"
    )
    class Meta:
        verbose_name="Товар"
        verbose_name_plural="Товары"

    def sale_price(self):
        return round(self.price-self.price*self.discount/100, 2)

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
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
        )
    class Meta:
        verbose_name="Категорию"
        verbose_name_plural="Категории"

    def __str__(self):
        return f'{self.text}'
from django.db import models


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='media/product_images/', verbose_name='Изображение', null=True, blank=True)
    product_category = models.CharField(max_length=150, verbose_name='Категория')
    product_price = models.IntegerField(verbose_name='Цена')
    date_creation = models.DateField(verbose_name='Дата создания')
    date_last_change = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.product_name}, {self.description}, {self.product_price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Наименование категории')
    description = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return f'{self.category_name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)

from django.db import models
#from blog.models import NULLABLE
from users.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Наименование категории')
    description = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return f'{self.category_name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='media/pic.png/', verbose_name='Изображение', null=True, blank=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    product_price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Создатель')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    def __str__(self):
        return f'{self.product_name}, {self.description}, {self.product_price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)
        permissions = [('can_change_description', 'Can change product description',),
                       ('can_change_category', 'Can change product category',),
                       ('set_published_status', 'Can change product published status',)]

class Contacts(models.Model):
    city = models.CharField(max_length=50, verbose_name="Страна")
    address = models.TextField(verbose_name="Адрес")
    slug = models.CharField(max_length=255, verbose_name="URL")

    def __str__(self):
        return f"{self.city} {self.address}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    numbers_version = models.IntegerField(verbose_name='Номер версии')
    name = models.CharField(verbose_name='Название версии')
    is_active = models.BooleanField(default=False, verbose_name='Активная версия')

    def __str__(self):
        return f'{self.numbers_version}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
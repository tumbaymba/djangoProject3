from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='Аватар', **NULLABLE)
    country = models.CharField(max_length=70, verbose_name='Страна', **NULLABLE)
    #token = models.CharField(max_length=80, verbose_name='Token', **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    '''@receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            User.objects.create(user=instance)'''

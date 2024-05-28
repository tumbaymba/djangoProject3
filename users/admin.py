from django.contrib import admin
from users.models import User


# Register your models here.


@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['is_active', 'is_staff', 'is_superuser', 'email']


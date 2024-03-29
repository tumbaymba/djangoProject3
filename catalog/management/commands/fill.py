from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'category_name': 'одежда', 'description': 'одежда и белье'},
            {'category_name': 'двери', 'description': 'двери для дома'},
            {'category_name': 'сантехника', 'description': 'раковины, ванные'},
            {'category_name': 'посуда', 'description': 'чашки, тарелки, блюдца'},
        ]

        category_for_creation = []
        for category_item in category_list:
            category_for_creation.append(Category(**category_item))

        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_creation)

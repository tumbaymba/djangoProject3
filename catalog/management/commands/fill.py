from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'category_name': 'овощи', 'description': 'огурцы, помидоры и пр.'},
            {'category_name': 'фрукты', 'description': 'апельсины, яблоки и пр.'},
            {'category_name': 'кондитерские изделия', 'description': 'торты, выпечка и пр.'},
            {'category_name': 'зелень', 'description': 'укроп, петрушка и пр.'},
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)

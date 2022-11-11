from django.core.management.base import BaseCommand

from core.management.data.test_menu import DATA
from core.models import FoodCategory


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.fill_categories()

    @staticmethod
    def fill_categories():
        print('fill categories')
        to_create = []
        if FoodCategory.objects.count() > 0:
            print('already filled')
            return
        else:
            for cat in DATA:
                to_create.append(FoodCategory(
                    id=cat["id"],
                    name_ru=cat["name_ru"],
                    name_en=cat["name_en"],
                    name_ch=cat["name_ch"],
                    order_id=cat["order_id"],
                ))
            FoodCategory.objects.bulk_create(to_create)

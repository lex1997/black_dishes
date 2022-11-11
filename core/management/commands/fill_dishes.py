from django.core.management.base import BaseCommand

from core.management.data.test_menu import DATA
from core.models import Food, FoodCategory


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.fill_dishes()

    @staticmethod
    def fill_dishes():
        print('fill dishes')
        to_create = []
        if Food.objects.count() > 0:
            print('already filled')
            return
        else:
            for cat in DATA:
                if cat["foods"]:
                    for i in cat["foods"]:
                        to_create.append(Food(
                            id=i["id"],
                            category=FoodCategory.objects.get(id=i["category"]),
                            internal_code=i["internal_code"],
                            code=i["code"],
                            name_ru=i["name_ru"],
                            description_ru=i["description_ru"],
                            description_en=i["description_en"],
                            description_ch=i["description_ch"],
                            is_vegan=i["is_vegan"],
                            is_special=i["is_special"],
                            cost=i["cost"],
                            is_publish=i["is_publish"]
                        ))
            Food.objects.bulk_create(to_create)



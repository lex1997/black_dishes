from django.db.models import Prefetch
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny

from config.settings.defaults import DEBUG
from core.models import Food, FoodCategory
from core.serializers import FoodCategorySerializer, FoodSerializer, MenuSerializer


class ResultPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10000


class DishesViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.filter()
    serializer_class = FoodSerializer
    if not DEBUG:
        permission_classes = (IsAuthenticated,)
        pagination_class = ResultPagination


class CategoriesOfDishesViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer
    if not DEBUG:
        permission_classes = (IsAuthenticated,)


class FoodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FoodCategory.objects.filter(
        food__is_publish=True
    ).prefetch_related(Prefetch("food", queryset=Food.objects.filter(is_publish=True))).distinct()
    serializer_class = MenuSerializer
    permission_classes = (AllowAny,)

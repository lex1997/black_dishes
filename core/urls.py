from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.views import DishesViewSet, CategoriesOfDishesViewSet, FoodViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


router = routers.SimpleRouter()
router.register(r'foods', FoodViewSet)
router.register(r'dishes', DishesViewSet)
router.register(r'categories', CategoriesOfDishesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

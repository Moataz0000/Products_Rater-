from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, RatingViewSet, CategoriesViewSet


router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('ratings', RatingViewSet)
router.register('categories', CategoriesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
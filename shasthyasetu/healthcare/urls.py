from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HealthDataViewSet, HealthTipViewSet

router = DefaultRouter()
router.register(r'health-data', HealthDataViewSet)
router.register(r'health-tips', HealthTipViewSet)

urlpatterns = [
    path('', include(router.urls)),
]












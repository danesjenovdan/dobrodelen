from django.urls import path, include
from rest_framework import routers

from .views import OrganizationViewSet


router = routers.DefaultRouter()
router.register(r'organizations', OrganizationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

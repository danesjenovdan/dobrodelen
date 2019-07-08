from rest_framework import viewsets, filters

from .models import Organization
from .serializers import OrganizationSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.filter(published=True)
    serializer_class = OrganizationSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ("criteria__stars",)
    ordering = ("-criteria__stars",)

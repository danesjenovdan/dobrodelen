from rest_framework import viewsets, filters, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core import signing

from .models import Organization
from .serializers import OrganizationSerializer, OrganizationDetailSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ("criteria__stars",)
    ordering = ("-criteria__stars",)

    def get_permissions(self):
        if self.action in ["list", "create"]:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.action not in ["list"] and self.is_valid_edit_key():
            return Organization.objects.all()
        return Organization.objects.filter(published=True)

    def get_serializer_class(self):
        if self.action == "create":
            return OrganizationDetailSerializer
        if self.action != "list" and self.is_valid_edit_key():
            return OrganizationDetailSerializer
        return OrganizationSerializer

    def is_valid_edit_key(self):
        edit_key = self.request.query_params.get("edit_key")
        if edit_key:
            try:
                org_id = signing.loads(edit_key, salt="ORG_EDIT_KEY")
                if self.detail:
                    return self.kwargs.get("pk") == str(org_id)
            except:
                pass
        return False

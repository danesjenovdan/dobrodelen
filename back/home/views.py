from rest_framework import viewsets, filters, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.core import signing

from home import serializers, models


class OrganizationViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ("criteria__stars",)
    ordering = ("-criteria__stars",)

    def get_permissions(self):
        if self.action in ["list", "create"]:
            permission_classes = [permissions.AllowAny]
        elif self.is_valid_edit_key():
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.action not in ["list"] and self.is_valid_edit_key():
            return models.Organization.objects.all()
        return models.Organization.objects.filter(published=True)

    def get_serializer_class(self):
        if self.action == "create":
            return serializers.OrganizationDetailSerializer
        if self.action != "list" and self.is_valid_edit_key():
            return serializers.OrganizationDetailSerializer
        return serializers.OrganizationSerializer

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

class OrganizationChildAuth(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action in ["create"]:
            permission_classes = [permissions.AllowAny]
        elif self.is_valid_edit_key():
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def is_valid_edit_key(self):
        edit_key = self.request.query_params.get("edit_key")
        print(edit_key)
        if edit_key:
            try:
                org_id = signing.loads(edit_key, salt="ORG_EDIT_KEY")
                print(org_id)
                obj = self.get_queryset().filter(pk=self.kwargs.get("pk"))
                print(obj)
                if obj:
                    print(obj[0].organization_id == org_id)
                    return obj[0].organization_id == org_id
            except Exception as e:
                print(e)
        return False

class BoardViewSet(OrganizationChildAuth):
    serializer_class = serializers.BoardSerializer
    queryset = models.Board.objects.all()

class BoardMemberViewSet(OrganizationChildAuth):
    serializer_class = serializers.BoardMemberSerializer
    queryset = models.BoardMember.objects.all()

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
        if self.action == "partial_update" and self.is_valid_edit_key():
            return serializers.OrganizationDetailSerializer
        if self.action == "retrieve" and self.is_valid_edit_key():
            return serializers.OrganizationDetailSerializer
        if self.action == "retrieve":
            return serializers.OrganizationPublicSerializer
        if self.action == "list":
            return serializers.OrganizationListSerializer
        return serializers.OrganizationListSerializer

    def is_valid_edit_key(self):
        edit_key = self.request.query_params.get("edit_key")
        if edit_key:
            try:
                org_id = signing.loads(edit_key, salt="ORG_EDIT_KEY")
                if self.detail:
                    return self.kwargs.get("pk") == str(org_id)
            except Exception as e:
                print(e)
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
        if edit_key:
            try:
                org_id = signing.loads(edit_key, salt="ORG_EDIT_KEY")
                obj = self.get_queryset().filter(pk=self.kwargs.get("pk"))
                if obj:
                    return obj[0].organization_id == org_id
            except Exception as e:
                print(e)
        return False


# class BoardMemberViewSet(OrganizationChildAuth):
#     serializer_class = serializers.BoardMemberSerializer
#     queryset = models.BoardMember.objects.all()


class LinkViewSet(OrganizationChildAuth):
    serializer_class = serializers.LinkSerializer
    queryset = models.Link.objects.all()


# __ FILLDATA __


def _fill_areas():
    areas = [
        (1, "Развој на граѓанското општество"),
        (2, "Демократија и владеење на правото"),
        (3, "Човекови права и антидискриминација"),
        (4, "Заштита на маргинализираните лица"),
        (5, "Родова еднаквост"),
        (6, "Земјоделство и рурален развој"),
        (7, "Медиуми и информатичко општество"),
        (8, "Спорт, хоби и рекреација"),
        (9, "Ненасилство и толеранција"),
        (10, "Економски и одржлив развој"),
        (11, "Наука, образование и доживотно учење"),
        (12, "Млади"),
        (13, "Социјална заштита и заштита на децата"),
        (14, "Заштита на здравјето"),
        (15, "Заштита на животната средина"),
        (16, "Култура"),
        (17, "Интеграции во ЕУ и политики"),
        (18, "Струкови (професионални) здруженија"),
        (19, "Друго:"),
    ]
    ids = list(range(1, len(areas) + 1))
    models.Area.objects.exclude(id__in=ids).delete()

    for id, name in areas:
        area, created = models.Area.objects.get_or_create(
            id=id, defaults={"name": name}
        )
        if not created:
            area.name = name
            area.save()
    print("done _fill_areas")


def _fill_regions():
    regions = [
        (1, "Вардарски"),
        (2, "Источен"),
        (3, "Југозападен"),
        (4, "Југоисточен"),
        (5, "Пелагониски"),
        (6, "Полошки"),
        (7, "Североисточен"),
        (8, "Скопски"),
    ]
    ids = list(range(1, len(regions) + 1))
    models.Region.objects.exclude(id__in=ids).delete()

    for id, name in regions:
        region, created = models.Region.objects.get_or_create(
            id=id, defaults={"name": name}
        )
        if not created:
            region.name = name
            region.save()
    print("done _fill_regions")


def fill():
    _fill_areas()
    _fill_regions()
    return "done"

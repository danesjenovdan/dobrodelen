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
        (1, "Človekove pravice, demokracija in enakost"),
        (2, "Izobraževanje, raziskave in razvoj"),
        (3, "Kultura"),
        (4, "Mladina, otroci"),
        (5, "Razvojno sodelovanje"),
        (6, "Sociala"),
        (7, "Šport"),
        (8, "Okolje, narava in prostor"),
        (9, "Zdravje"),
        (11, "Starejši"),
        (10, "Drugo (navedite kaj):"),
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
        (1, "Gorenjska"),
        (2, "Goriška"),
        (3, "Jugovzhodna Slovenija"),
        (4, "Koroška"),
        (5, "Notranjskokraška"),
        (6, "Obalnokraška"),
        (7, "Osrednjeslovenska"),
        (8, "Podravska"),
        (9, "Pomurska"),
        (10, "Posavska"),
        (11, "Savinjska"),
        (12, "Zasavska"),
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

import re
import requests

from django.core import signing
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework import filters, permissions, status, views, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from home import models, qrcode, serializers


class OrganizationViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.OrderingFilter,)
    # TODO: fix
    # ordering_fields = ("criteria__points",)
    # ordering = ("-criteria__points",)

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
        if self.action == "update" and self.is_valid_edit_key():
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


class OrganizationFilteredCriteria(views.APIView):
    def get_queryset(self):
        # TODO: fix
        # order_by = "-criteria__points"
        # ordering = self.request.query_params.get("ordering")
        # if ordering and ordering == "criteria__points":
        #     order_by = "criteria__points"

        return models.Organization.objects.filter(published=True)  # .order_by(order_by)

    def get(self, request, format=None):
        # TODO: fix
        # all_keys = set(models.Criteria.max_values.keys())
        # query_keys = self.request.query_params.get("filter_keys", "").split(",")
        # filter_keys = list(all_keys.intersection(query_keys))

        # points = {
        #     org.id: org.compute_filtered_points(filter_keys)
        #     for org in self.get_queryset()
        # }

        serializer = serializers.OrganizationListSerializer(
            self.get_queryset(), many=True
        )
        data = serializer.data

        # for entry in data:
        #     entry["stars"] = -1
        #     entry["points"] = points[entry["id"]]

        return Response({"results": data})


class OrganizationDonationQrCode(View):
    def get_queryset(self):
        return models.Organization.objects.filter(published=True)

    def get_object(self, pk):
        return get_object_or_404(self.get_queryset(), pk=pk)

    def get(self, request, pk, *args, **kwargs):
        amount_string = request.GET.get("amount")
        try:
            amount = int(amount_string)
            if amount < 1:
                return HttpResponse(
                    "amount needs to be positive", status=status.HTTP_400_BAD_REQUEST
                )
        except (TypeError, ValueError):
            return HttpResponse(
                "amount needs to be an integer", status=status.HTTP_400_BAD_REQUEST
            )

        org = self.get_object(pk)

        address_parts = org.address.rsplit(",", maxsplit=1)
        address1 = address_parts[0]
        address2 = address_parts[1] if len(address_parts) > 1 else ""

        iban = re.sub(r"^SI56", "", org.account_number.strip())
        iban = re.sub(r"[^0-9]", "", iban)
        if not iban:
            return HttpResponse(
                "organization is missing account_number",
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not iban.startswith("SI56"):
            iban = "SI56" + iban
        if len(iban) != 19:
            return HttpResponse(
                "organization has an invalid account_number",
                status=status.HTTP_400_BAD_REQUEST,
            )

        qr_svg = qrcode.generate_upn_qr(
            org.name,
            address1,
            address2,
            iban,
            "SI99",
            "Donacija preko dobrodelen.si",
            amount,
        )

        return HttpResponse(qr_svg, content_type="image/svg+xml")


class OrganizationHasTaxDonation(View):
    def get_queryset(self):
        return models.Organization.objects.filter(published=True)

    def get_object(self, pk):
        return get_object_or_404(self.get_queryset(), pk=pk)

    def get(self, request, pk, *args, **kwargs):
        org = self.get_object(pk)

        if org.tax_number and len(org.tax_number) == 8:
            try:
                response = requests.get(
                    f"https://www.cnvos.si/enprocent/findNGOByTaxNumber/{org.tax_number}/",
                    timeout=10,
                )
                if response.ok:
                    if "application/json" in response.headers.get("Content-Type", ""):
                        data = response.json()
                        if data["found"]:
                            return JsonResponse(data)
            except requests.exceptions.Timeout:
                return JsonResponse({"found": False, "timeout": True})

        return JsonResponse({"found": False})


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

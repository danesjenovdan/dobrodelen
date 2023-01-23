from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import fields, serializers
from wagtail.images import get_image_model
from wagtail.images.api.fields import ImageRenditionField

from .models import Link, Organization


class ImageRenditionAndUploadField(ImageRenditionField):
    def to_internal_value(self, data):
        if data:
            # defer image validation to rest framework image field
            clean_data = fields.ImageField().to_internal_value(data)
            # get wagtail image model and create the image
            Image = get_image_model()
            return Image.objects.create(title=clean_data._name, file=clean_data)


class LinkSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Link
        fields = ("url",)


class OrganizationListSerializer(serializers.ModelSerializer):
    cover_photo = ImageRenditionAndUploadField("original")

    class Meta:
        model = Organization
        fields = (
            "id",
            "name",
            "additional_names",
            "description",
            "cover_photo",
            "area",
            "avg_revenue",
            "employed",
            "is_charity",
            "has_public_interest",
            "is_voluntary",
            "zero5",
            "zero5_amount",
            "region",
            # TODO: fix this
            # "stars",
            # "points",
        )


class OrganizationPublicSerializer(serializers.ModelSerializer):
    cover_photo = ImageRenditionAndUploadField("original")
    area = serializers.SerializerMethodField(required=False)
    region = serializers.SerializerMethodField(required=False)
    links = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Organization
        fields = (
            "id",
            "name",
            "additional_names",
            "description",
            "address",
            "contact_name",
            "contact_email",
            "contact_phone",
            "web_page",
            "links",
            "cover_photo",
            "tax_number",
            "account_number",
            "donation_url",
            "area",
            "avg_revenue",
            "employed",
            "is_charity",
            "has_public_interest",
            "is_voluntary",
            "zero5",
            "zero5_amount",
            "region",
            # TODO: fix this
            # "stars",
            # "points",
            # "points_details",
        )

    def get_area(self, obj):
        areas = obj.area.all()
        if areas:
            # 10 is the id of other
            has_other = len(areas.filter(id=10)) > 0
            area_list = list(areas.exclude(id=10).values_list("name", flat=True))
            if has_other and obj.custom_area:
                area_list.append(obj.custom_area)
            return area_list
        return []

    def get_region(self, obj):
        regions = obj.region.all()
        if regions:
            return list(regions.values_list("name", flat=True))
        return []

    def get_links(self, obj):
        return obj.links.values_list("url", flat=True)


class OrganizationDetailSerializer(WritableNestedModelSerializer):
    cover_photo = ImageRenditionAndUploadField(
        "original",
        required=False,
        allow_null=True,
    )
    links = LinkSerializer(
        many=True,
        required=False,
    )

    class Meta:
        model = Organization
        fields = (
            "id",
            "name",
            "additional_names",
            "description",
            "address",
            "contact_name",
            "contact_email",
            "contact_phone",
            "web_page",
            "links",
            "cover_photo",
            "tax_number",
            "account_number",
            "donation_url",
            "area",
            "avg_revenue",
            "employed",
            "is_charity",
            "has_public_interest",
            "is_voluntary",
            "zero5",
            "zero5_amount",
            "region",
            # TODO: add all fields here
            # TODO: fix this
            # "stars",
            # "points",
            # "points_details",
        )

from rest_framework import serializers, fields
from wagtail.images.api.fields import ImageRenditionField
from wagtail.images import get_image_model

from .models import Organization


class ImageRenditionAndUploadField(ImageRenditionField):
    def to_internal_value(self, data):
        if data:
            # defer image validation to rest framework image field
            clean_data = fields.ImageField().to_internal_value(data)
            # get wagtail image model and create the image
            Image = get_image_model()
            return Image.objects.create(title=clean_data._name, file=clean_data)


class OrganizationSerializer(serializers.ModelSerializer):
    cover_photo = ImageRenditionAndUploadField("original")

    class Meta:
        model = Organization
        fields = ("id", "name", "description", "cover_photo", "stars")


class OrganizationDetailSerializer(serializers.ModelSerializer):
    cover_photo = ImageRenditionAndUploadField("original")

    class Meta:
        model = Organization
        fields = (
            "id",
            "name",
            "description",
            "cover_photo",
            "stars",
            "signup_time",
            "edit_key",
        )

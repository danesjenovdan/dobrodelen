from rest_framework import serializers
from wagtail.images.api.fields import ImageRenditionField

from .models import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    cover_photo = ImageRenditionField("original")

    class Meta:
        model = Organization
        fields = ("id", "name", "description", "cover_photo", "stars")

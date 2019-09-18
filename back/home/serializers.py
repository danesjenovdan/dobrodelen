from rest_framework import serializers, fields
from wagtail.images.api.fields import ImageRenditionField
from wagtail.images import get_image_model

from drf_writable_nested import WritableNestedModelSerializer

from home import models


class ImageRenditionAndUploadField(ImageRenditionField):
    def to_internal_value(self, data):
        if data:
            # defer image validation to rest framework image field
            clean_data = fields.ImageField().to_internal_value(data)
            # get wagtail image model and create the image
            Image = get_image_model()
            return Image.objects.create(title=clean_data._name, file=clean_data)


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = ("id", "name", "role")


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Board
        fields = ("id", "name", "meeting_dates", "organization")


class LinkSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.Link
        fields = ("url",)


class BoardMemberSerializer(WritableNestedModelSerializer):
    member = MemberSerializer()

    class Meta:
        model = models.BoardMember
        fields = ("id", "member", "board", "organization", "is_paid")


class OrganizationListSerializer(serializers.ModelSerializer):
    cover_photo = ImageRenditionAndUploadField("original")

    class Meta:
        model = models.Organization
        fields = ("id", "name", "description", "cover_photo", "stars")


class OrganizationPublicSerializer(serializers.ModelSerializer):
    cover_photo = ImageRenditionAndUploadField("original")
    area = serializers.SerializerMethodField(required=False)
    links = serializers.SerializerMethodField(required=False)

    class Meta:
        model = models.Organization
        fields = (
            "id",
            "name",
            "additional_names",
            "contact_name",
            "contact_email",
            "contact_phone",
            "web_page",
            "description",
            "cover_photo",
            "stars",
            "links",
            "area",
            "mission",
            "avg_revenue",
            "employed",
            "is_charity",
            "has_public_interest",
            "is_voluntary",
            "zero5",
            "edit_key",  # TODO: remove when on production
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

    def get_links(self, obj):
        return obj.links.values_list("url", flat=True)


class OrganizationDetailSerializer(WritableNestedModelSerializer):
    cover_photo = ImageRenditionAndUploadField("original", required=False)
    boards = BoardSerializer(many=True, required=False, read_only=True)
    board_members = serializers.SerializerMethodField(required=False)
    links = LinkSerializer(many=True, required=False)

    class Meta:
        model = models.Organization
        fields = (
            "id",
            "name",
            "additional_names",
            "contact_name",
            "contact_email",
            "contact_phone",
            "web_page",
            "description",
            "tax_number",
            "mission",
            "area",
            "custom_area",
            "avg_revenue",
            "employed",
            "is_charity",
            "has_public_interest",
            "is_voluntary",
            "zero5",
            "strategic_planning",
            "milestiones_description",
            "has_milestiones_description",
            "wages_ratio",
            "boards",
            "board_members",
            "links",
            "minutes_meeting",
            "has_minutes_meeting",
            "strategic_goals",
            "has_strategic_goals",
            "finance_report",
            "finance_report_ajpes",
            "audited_report",
            "has_audited_report",
            "finance_plan",
            "has_finance_plan",
            "given_loan",
            "has_given_loans",
            "received_loans",
            "has_received_loans",
            "payment_classes",
            "has_payment_classes",
            "cover_photo",
            "stars",
            "signup_time_start",
            "signup_time",
            "is_complete",
            "edit_key",
        )

    def get_board_members(self, obj):
        members = obj.board_members.all()
        board_members = models.BoardMember.objects.filter(
            member__in=members, organization=obj
        )
        ll = BoardMemberSerializer(board_members, many=True)
        return ll.data

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


class LinkSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.Link
        fields = ("url",)


class SupervisoryBoardMemberSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.SupervisoryBoardMember
        fields = ("id", "name", "role", "custom_role", "is_paid")


class ManagementBoardMemberSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.ManagementBoardMember
        fields = ("id", "name", "role", "custom_role", "is_paid")


class CouncilBoardMemberSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.CouncilBoardMember
        fields = ("id", "name", "role", "custom_role", "is_paid")


class OtherBoardMemberSerializer(WritableNestedModelSerializer):
    class Meta:
        model = models.OtherBoardMember
        fields = ("id", "name", "role", "custom_role", "is_paid")


class OrganizationListSerializer(serializers.ModelSerializer):
    cover_photo = ImageRenditionAndUploadField("original")

    class Meta:
        model = models.Organization
        fields = (
            "id",
            "name",
            "additional_names",
            "description",
            "cover_photo",
            "stars",
            "is_charity",
            "has_public_interest",
            "is_voluntary",
            "area",
            "avg_revenue",
            "employed",
            "zero5",
        )


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
            "points",
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
    cover_photo = ImageRenditionAndUploadField(
        "original", required=False, allow_null=True
    )
    links = LinkSerializer(many=True, required=False)
    supervisory_board_members = SupervisoryBoardMemberSerializer(
        many=True, required=False
    )
    management_board_members = ManagementBoardMemberSerializer(
        many=True, required=False
    )
    council_members = CouncilBoardMemberSerializer(many=True, required=False)
    other_board_members = OtherBoardMemberSerializer(many=True, required=False)

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
            "has_published_work_reports",
            "published_work_reports_url",
            "has_published_financial_reports",
            "published_financial_reports_url",
            "has_published_executive_salaries",
            "published_executive_salaries_url",
            "has_published_salary_ratio",
            "published_salary_ratio_url",
            "has_published_employee_list",
            "published_employee_list_url",
            "has_published_board_members",
            "published_board_members_url",
            "has_published_financial_plan",
            "published_financial_plan_url",
            "has_supervisory_board",
            "supervisory_board_dates",
            "supervisory_board_members",
            "has_management_board",
            "management_board_dates",
            "management_board_members",
            "has_council",
            "council_dates",
            "council_members",
            "has_other_board",
            "other_board_name",
            "other_board_dates",
            "other_board_members",
            "has_minutes_meeting",
            "minutes_meeting",
        )

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
            # META INFO
            # "is_complete",
            # "signup_time_start",
            # "signup_time",
            # OSEBNA IZKAZNICA ORGANIZACIJE
            "name",
            "additional_names",
            "cover_photo",
            # "address",
            # "contact_name",
            # "contact_email",
            # "contact_phone",
            # "tax_number",
            # "account_number",
            # "donation_url",
            # "web_page",
            # "links",
            "region",
            "area",
            "custom_area",
            # SCORE
            "stars",
            "points",
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
            # META INFO
            "is_complete",
            "signup_time_start",
            "signup_time",
            # OSEBNA IZKAZNICA ORGANIZACIJE
            "name",
            "additional_names",
            "cover_photo",
            "address",
            "contact_name",
            "contact_email",
            "contact_phone",
            "tax_number",
            "account_number",
            "donation_url",
            "web_page",
            "links",
            "region",
            "area",
            "custom_area",
            # REVIEW INFO
            "review_date",
            # SCORE
            "stars",
            "points",
            "points_details",
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
            "edit_key",
            # META INFO
            "is_complete",
            "signup_time_start",
            "signup_time",
            # OSEBNA IZKAZNICA ORGANIZACIJE
            "name",
            "additional_names",
            "cover_photo",
            "address",
            "contact_name",
            "contact_email",
            "contact_phone",
            "tax_number",
            "account_number",
            "donation_url",
            "web_page",
            "links",
            "region",
            "area",
            "custom_area",
            # DOSTOPNOST OSNOVNIH INFORMACIJ
            "has_published_key_documents",
            "key_documents_url",
            "has_published_mission",
            "mission_url",
            "has_published_key_employee_list",
            "key_employee_list_url",
            "has_published_board_member_list",
            "board_member_list_url",
            "has_published_contact_information",
            "contact_information_url",
            "has_published_complaints_contact",
            "complaints_contact_url",
            "has_published_complaints_process",
            "complaints_process_url",
            # DOSTOPNOST VSEBINSKIH POROČIL
            "has_published_substantive_report",
            "substantive_report_url",
            "has_published_report_about_work",
            "report_about_work_url",
            "has_published_report_with_results",
            "report_with_results_url",
            "has_published_work_plan",
            "work_plan_url",
            "has_published_strategic_objectives",
            "strategic_objectives_url",
            # FINANČNA TRANSPARENTNOST
            "has_published_financial_report",
            "financial_report_url",
            "has_published_understandable_financial_report",
            "understandable_financial_report_url",
            "has_published_operating_expenses",
            "operating_expenses_url",
            "has_published_main_sources_of_financing",
            "main_sources_of_financing_url",
            "has_published_management_revenues",
            "management_revenues_url",
            "has_published_salary_ratio",
            "salary_ratio_url",
            # ZBIRANJE DONACIJSKIH SREDSTEV
            "has_published_fundraising_reports",
            "fundraising_reports_url",
            "has_published_fundraising_report_with_purposes",
            "fundraising_report_with_purposes_url",
            # DOSTOP OBJAVLJENIH INFORMACIJ
            "website_accessibility_contrast",
            "website_accessibility_zoom",
            "website_accessibility_disabilities",
            # REVIEW INFO
            "review_date",
            "review_notes",
            "published",
            # SCORE
            "stars",
            "points",
            "points_details",
        )

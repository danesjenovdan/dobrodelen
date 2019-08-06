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
        fields = (
            'id',
            'name',
            'role'
        )


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Board
        fields = (
            'id',
            'name',
            'meeting_dates',
            'organization'
        )


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Link
        fields = (
            'id',
            'name',
            'url',
            'organization'
        )

class BoardMemberSerializer(WritableNestedModelSerializer):
    member = MemberSerializer()
    class Meta:
        model = models.BoardMember
        fields = (
            'id',
            'member',
            'board',
            'organization',
            'is_paid'
        )


class OrganizationListSerializer(serializers.ModelSerializer):
    cover_photo = ImageRenditionAndUploadField('original')

    class Meta:
        model = models.Organization
        fields = ('id', 'name', 'description', 'cover_photo', 'stars')


class OrganizationPublicSerializer(serializers.ModelSerializer):
    cover_photo = ImageRenditionAndUploadField('original')
    links = LinkSerializer(many=True)
    area = serializers.SerializerMethodField(required=False)
    class Meta:
        model = models.Organization
        fields = (
            'id',
            'name',
            'additional_names',
            'contact_info',
            'web_page',
            'description',
            'cover_photo',
            'stars',
            'links',
            'area',
            'mission',
            'avg_revenue',
            'employed',
            'is_charity',
            'has_public_interest',
            'is_voluntary',
            'zero5'
        )
    def get_area(self, obj):
        areas = obj.area.all()
        if areas:
            return ', '.join(list(areas.values_list('name', flat=True)))
        else:
            return obj.custom_area

class OrganizationDetailSerializer(serializers.ModelSerializer):
    cover_photo = ImageRenditionAndUploadField('original', required=False)
    boards = BoardSerializer(many=True, required=False, read_only=True)
    board_members = serializers.SerializerMethodField(required=False)

    class Meta:
        model = models.Organization
        fields = (
            'id',
            'name',
            'additional_names',
            'contact_info',
            'web_page',
            'description',
            'tax_number',
            'mission',
            'area',
            'avg_revenue',
            'employed',
            'is_charity',
            'has_public_interest',
            'is_voluntary',
            'zero5',
            'strategic_planning',
            'milestiones_description',
            'wages_ratio',
            'boards',
            'board_members',

            'minutes_meeteng',
            'strategic_goals',
            'finance_report',
            'finance_report_ajpes',
            'audited_report',
            'finance_plan',
            'given_loan',
            'received_loans',
            'payment_classes',

            'cover_photo',

            'stars',
            'signup_time',
            'edit_key',
        )
    def get_board_members(self, obj):
        members = obj.board_members.all()
        board_members = BoardMember.objects.filter(member__in=members, organization=obj)
        ll = BoardMemberSerializer(board_members, many=True)
        return ll.data

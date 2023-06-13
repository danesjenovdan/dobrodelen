from django.urls import path, include
from rest_framework import routers

from home import views


router = routers.DefaultRouter()
router.register(r"organizations", views.OrganizationViewSet, basename="organization")
# router.register(r"boardmembers", views.BoardMemberViewSet, basename="boardmembers")
router.register(r"links", views.LinkViewSet, basename="links")


urlpatterns = [
    path(
        "organizations-filtered-criteria/",
        views.OrganizationFilteredCriteria.as_view(),
        name="organizations-filtered-criteria",
    ),
    path(
        "organizations-donation-qr-code/<int:pk>/",
        views.OrganizationDonationQrCode.as_view(),
        name="organizations-donation-qr-code",
    ),
    path(
        "organization-has-tax-donation/<int:pk>/",
        views.OrganizationHasTaxDonation.as_view(),
        name="organization-has-tax-donation",
    ),
    path("", include(router.urls)),
]

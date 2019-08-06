from django.utils.html import format_html
from django.templatetags.static import static
from wagtail.core import hooks
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from home import models


class OrganizationModelAdmin(ModelAdmin):
    model = models.Organization
    menu_icon = "form"
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False
    list_display = ("name", "published")
    search_fields = ("name", "description")


class OrganizationAdminGroup(ModelAdminGroup):
    menu_label = "Organizacije"
    menu_icon = "folder-open-inverse"
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (OrganizationModelAdmin,)


class BoardModelAdmin(ModelAdmin):
    model = models.Board
    menu_icon = "form"
    menu_order = 250  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False
    list_display = ("name",)
    search_fields = ("name",)


class BoardAdminGroup(ModelAdminGroup):
    menu_label = "Odbori"
    menu_icon = "folder-open-inverse"
    menu_order = 250  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (BoardModelAdmin,)


class AreasModelAdmin(ModelAdmin):
    model = models.Area
    menu_icon = "form"
    menu_order = 300  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False
    list_display = ("name",)
    search_fields = ("name",)


class AreasAdminGroup(ModelAdminGroup):
    menu_label = "Območja delovanja"
    menu_icon = "folder-open-inverse"
    menu_order = 300  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (AreasModelAdmin,)


@hooks.register("insert_global_admin_css")
def global_admin_css():
    return format_html(
        '<link rel="stylesheet" href="{}">', static("wagtailadmin/css/home.css")
    )


modeladmin_register(OrganizationAdminGroup)
modeladmin_register(BoardAdminGroup)
modeladmin_register(AreasAdminGroup)

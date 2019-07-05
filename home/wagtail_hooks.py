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


modeladmin_register(OrganizationAdminGroup)

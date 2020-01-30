from django.utils.html import format_html
from django.templatetags.static import static
from wagtail.core import hooks
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from . import models


class OrganizationModelAdmin(ModelAdmin):
    model = models.Organization
    menu_icon = "form"
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False
    list_display = ("name", "published", "is_complete")
    list_filter = ("published", "is_complete")
    search_fields = ("name", "description")


class OrganizationAdminGroup(ModelAdminGroup):
    menu_label = "Organizacije"
    menu_icon = "folder-open-inverse"
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (OrganizationModelAdmin,)


modeladmin_register(OrganizationAdminGroup)


@hooks.register("insert_global_admin_css")
def global_admin_css():
    return format_html(
        '<link rel="stylesheet" href="{}">', static("wagtailadmin/css/home.css")
    )


@hooks.register("construct_main_menu")
def hide_explorer_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != "explorer"]


class DummyPanel:
    name = "dummy"
    order = 50

    def render(self):
        return ""


@hooks.register("construct_homepage_panels")
def hide_homepage_panels(request, panels):
    hidden = [
        "site_summary",
        "pages_for_moderation",
        "recent_edits",
        "upgrade_notification",
    ]
    panels[:] = [panel for panel in panels if panel.name not in hidden]
    # if there are no panels some default text gets rendered, prevent that
    panels.append(DummyPanel())
    pass

from django.contrib.admin import SimpleListFilter
from django.templatetags.static import static
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from wagtail.admin.site_summary import SummaryItem
from wagtail.admin.ui.components import Component
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)
from wagtail.core import hooks

from .models import Organization


class IsCompleteDefaultFilter(SimpleListFilter):
    title = "Je prijava končana?"
    parameter_name = "is_complete"

    def lookups(self, request, model_admin):
        return (
            ("all", _("All")),
            (None, _("Yes")),
            ("0", _("No")),
        )

    def choices(self, changelist):
        for lookup, title in self.lookup_choices:
            yield {
                "selected": self.value() == lookup,
                "query_string": changelist.get_query_string(
                    {
                        self.parameter_name: lookup,
                    },
                    [],
                ),
                "display": title,
            }

    def queryset(self, request, queryset):
        if self.value() == None:
            return queryset.filter(is_complete=True)
        if self.value() == "0":
            return queryset.filter(is_complete=False)
        if self.value() == "all":
            return queryset


class OrganizationModelAdmin(ModelAdmin):
    model = Organization
    menu_icon = "form"
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False
    list_display = ("name", "published", "is_complete")
    list_filter = ("published", IsCompleteDefaultFilter)
    search_fields = ("name", "additional_names")


class OrganizationAdminGroup(ModelAdminGroup):
    menu_label = "Organizacije"
    menu_icon = "folder-open-inverse"
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (OrganizationModelAdmin,)


modeladmin_register(OrganizationAdminGroup)


@hooks.register("construct_main_menu")
def hide_explorer_menu_item(request, menu_items):
    hidden = [
        "explorer",
        "help",
        "reports",
        "porocila",
    ]
    menu_items[:] = [item for item in menu_items if item.name not in hidden]


class DummyPanel(Component):
    name = "dummy"
    order = 50

    def render_html(self, parent_context):
        return ""


@hooks.register("construct_homepage_panels")
def hide_homepage_panels(request, panels):
    hidden = [
        # "site_summary",
        "pages_for_moderation",
        "recent_edits",
        "upgrade_notification",
    ]
    panels[:] = [panel for panel in panels if panel.name not in hidden]
    # if there are no panels some default text gets rendered, prevent that
    panels.append(DummyPanel())


class OrganizationsSummaryItem(SummaryItem):
    order = 300
    template_name = "home/admin/site_summary_organizations.html"

    def get_context_data(self, parent_context):
        url_helper = OrganizationModelAdmin().url_helper
        index_url = url_helper.get_action_url("index")

        count = Organization.objects.count()

        return {
            "index_url": index_url,
            "count": count,
        }


@hooks.register("construct_homepage_summary_items", order=1)
def change_homepage_summary_items(request, summary_items):
    hidden = [
        "PagesSummaryItem",
        "ImagesSummaryItem",
        # "DocumentsSummaryItem",
    ]
    summary_items[:] = [
        item for item in summary_items if item.__class__.__name__ not in hidden
    ]
    summary_items.append(OrganizationsSummaryItem(request))


@hooks.register("insert_global_admin_css")
def global_admin_css():
    return format_html(
        '<link rel="stylesheet" href="{}">', static("css/custom_admin.css")
    )


@hooks.register("insert_global_admin_js")
def global_admin_js():
    return format_html('<script src="{}"></script>', static("js/custom_admin.js"))

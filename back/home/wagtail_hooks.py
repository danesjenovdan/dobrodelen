from django.contrib.admin import SimpleListFilter
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from django.templatetags.static import static
from django.urls import re_path, reverse
from django.utils.decorators import method_decorator
from django.utils.html import format_html
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from wagtail.admin.site_summary import SummaryItem
from wagtail.admin.ui.components import Component
from wagtail.admin.views.mixins import ExcelDateFormatter
from wagtail.contrib.modeladmin.helpers import AdminURLHelper, ButtonHelper
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)
from wagtail.contrib.modeladmin.views import IndexView
from wagtail.core import hooks
from wagtail.images import get_image_model
from xlsxwriter.workbook import Workbook

from .models import Organization

Image = get_image_model()

# --- Export


class ExportButtonHelper(ButtonHelper):
    export_button_classnames = ["icon", "icon-download"]

    def export_button(self, classnames_add=None, classnames_exclude=None):
        if classnames_add is None:
            classnames_add = []
        if classnames_exclude is None:
            classnames_exclude = []

        classnames = self.export_button_classnames + classnames_add
        cn = self.finalise_classname(classnames, classnames_exclude)
        text = f"Prenesi seznam kot XLSX"

        return {
            "url": self.url_helper.get_action_url(
                "export", query_params=self.request.GET
            ),
            "label": text,
            "classname": cn,
            "title": text,
        }


class ExportAdminURLHelper(AdminURLHelper):
    non_object_specific_actions = ("create", "choose_parent", "index", "export")

    def get_action_url(self, action, *args, **kwargs):
        query_params = kwargs.pop("query_params", None)

        url_name = self.get_action_url_name(action)
        if action in self.non_object_specific_actions:
            url = reverse(url_name)
        else:
            url = reverse(url_name, args=args, kwargs=kwargs)

        if query_params:
            url += "?{params}".format(params=query_params.urlencode())

        return url

    def get_action_url_pattern(self, action):
        if action in self.non_object_specific_actions:
            return self._get_action_url_pattern(action)

        return self._get_object_specific_action_url_pattern(action)


class ExportView(IndexView):
    model_admin = None

    def export_xlsx(self):
        if not self.model_admin or not hasattr(
            self.model_admin, "get_xlsx_export_data"
        ):
            raise ImproperlyConfigured(
                "ExportView requires an implementation of 'get_xlsx_export_data()'"
            )

        data = self.model_admin.get_xlsx_export_data(self.queryset.all())

        if self.model_admin and hasattr(self.model_admin, "get_xlsx_export_filename"):
            filename = self.model_admin.get_xlsx_export_filename(self.queryset.all())
        else:
            model_name_slug = slugify(str(self.queryset.model.__name__))
            model_name_slug = model_name_slug.replace("-", "_")
            filename = f"{model_name_slug}_export.xlsx"

        response = HttpResponse(
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = f"attachment; filename={filename};"
        response["Cache-Control"] = "no-cache"

        if isinstance(data, list) and len(data):
            fieldnames = data[0].keys()

            workbook = Workbook(
                response,
                {
                    "in_memory": True,
                    "constant_memory": True,
                    "remove_timezone": True,
                    "default_date_format": ExcelDateFormatter().get(),
                },
            )
            worksheet = workbook.add_worksheet()

            for col_number, field in enumerate(fieldnames):
                worksheet.write(0, col_number, field)

            for row_number, row in enumerate(data):
                for col_number, (field, value) in enumerate(row.items()):
                    worksheet.write(row_number + 1, col_number, value)

            workbook.close()

        return response

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        return self.export_xlsx()


class ExportModelAdminMixin(object):
    button_helper_class = ExportButtonHelper
    url_helper_class = ExportAdminURLHelper
    export_view_class = ExportView
    index_template_name = "wagtailadmin/index_with_export.html"

    def get_admin_urls_for_registration(self):
        urls = super().get_admin_urls_for_registration()
        urls += (
            re_path(
                self.url_helper.get_action_url_pattern("export"),
                self.export_view,
                name=self.url_helper.get_action_url_name("export"),
            ),
        )
        return urls

    def export_view(self, request):
        kwargs = {"model_admin": self}
        view_class = self.export_view_class
        return view_class.as_view(**kwargs)(request)


# ---


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


class OrganizationModelAdmin(ExportModelAdminMixin, ModelAdmin):
    model = Organization
    menu_icon = "form"
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False
    list_display = ("name", "published", "is_complete")
    list_filter = ("published", IsCompleteDefaultFilter)
    search_fields = ("name", "additional_names")

    def get_xlsx_export_filename(self, queryset):
        return "dobrodelen_organizacije_export.xlsx"

    def get_xlsx_export_data(self, queryset):
        rows = list()

        if not len(queryset):
            return rows

        panel_fields = queryset[0].get_panel_fields()

        for item in queryset:
            row = dict()

            for field_name, field_verbose_name, field_parents in panel_fields:
                field_title = field_verbose_name
                field_value = getattr(item, field_name)

                if isinstance(field_value, bool):
                    field_value = "Da" if field_value else "Ne"
                if isinstance(field_value, Image):
                    field_value = field_value.file.name
                if field_value.__class__.__name__ == "ManyRelatedManager":
                    field_value = ", ".join([str(x) for x in field_value.all()])

                if field_verbose_name.startswith("Kriterij "):
                    field_title = field_verbose_name.replace("Kriterij ", "K")

                for field_parent in field_parents:
                    if field_parent.startswith("Sklop "):
                        prefix = field_parent.replace("Sklop ", "S").split(":")[0]
                        field_title = prefix + " " + field_title

                row[field_title] = field_value

            row["Točke"] = item.points
            row["Zvedzice"] = item.stars

            # pprint(row)
            rows.append(row)

        return rows


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

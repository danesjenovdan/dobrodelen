from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from home import models


class OrganizationModelAdmin(ModelAdmin):
    model = models.Organization
    # menu_label = 'Razpisi'  # ditch this to use verbose_name_plural from model
    menu_icon = 'date'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    #exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('name', 'published')
    #list_filter = (('name', DateRangeFilter), 'regije', 'vrsta', 'podrocja')
    search_fields = ('name', 'description',)



class OrganizationAdminGroup(ModelAdminGroup):
    menu_label = 'Organizacije'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (OrganizationModelAdmin,)  # RegijaModelAdmin, PodrocjeModelAdmin

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(OrganizationAdminGroup)

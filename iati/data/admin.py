# Django specific
from django.contrib import admin

# App specific
from data.models.activity import IATIActivity
from data.models.organisation import Organisation

class OrganistaionAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'ref', 'total_activities']

class IATIActivityAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'reporting_organisation', 'is_active', 'date_updated']
    list_filter = ('reporting_organisation__org_name',)

admin.site.register(IATIActivity, IATIActivityAdmin)
admin.site.register(Organisation, OrganistaionAdmin)
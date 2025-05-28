from django.contrib import admin
from .models import Patient

# Register your models here.
admin.site.site_header = 'Patient Management System'
admin.site.site_title = 'Patient Management System'

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_names', 'surname')
    search_fields = ('first_names', 'surname')
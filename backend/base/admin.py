from django.contrib import admin
from .models import EMP

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user','name','adresse','poste','department','salary','nbrAbsences')

admin.site.register(EMP, EmployeeAdmin)
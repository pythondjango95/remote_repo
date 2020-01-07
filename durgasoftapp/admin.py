from django.contrib import admin
from durgasoftapp.models import (Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['CNumber', 'CName', 'CFaculty', 'CDuration', 'CContent']

admin.site.register(Service,ServiceAdmin)


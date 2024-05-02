from django.contrib import admin
from .models import Number_store
# from import_export.admin import ImportExportModelAdmin
from .models import FileUpload


# @admin.register(Number_store)
# class userData(ImportExportModelAdmin):
#     pass

admin.register(Number_store)
admin.site.register(FileUpload)

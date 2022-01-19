from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


@admin.register(ExcelsheetData)
class exceldata(ImportExportModelAdmin):
    list_display = ['id','case_no','case_code','file_no','case_id','case_status','loan_type', 'name', 'address','city','phone1','phone2','landmark']



admin.site.register(CustomUser)
admin.site.register(VApp)
admin.site.register(SiteVisit)
admin.site.register(Issue)
admin.site.register(RoleRef)
admin.site.register(FieldReport)
# admin.site.register(BankSubmission)

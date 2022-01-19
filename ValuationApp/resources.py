from import_export import resources
from .models import ExcelsheetData

class ExcelsheetDataResource(resources.ModelResource):
    class meta:
        model=ExcelsheetData

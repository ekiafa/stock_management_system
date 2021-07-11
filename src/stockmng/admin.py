from django.contrib import admin
from .forms import StockCreateForm
# Register your models here.

from .models import Stock
from import_export.admin import ImportExportModelAdmin



class StockCreateAdmin(ImportExportModelAdmin):
    list_display=['symbol','name','sector']
    form=StockCreateForm    
    pass


admin.site.register(Stock,StockCreateAdmin)

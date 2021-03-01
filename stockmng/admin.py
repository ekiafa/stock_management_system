from django.contrib import admin
from .forms import StockCreateForms
# Register your models here.

from .models import Stock


class StockCreateAdmin(admin.ModelAdmin):
    list_display=['category','item_name','quantity']
    form=StockCreateForm

admin.site.register(Stock,StockCreateAdmin)

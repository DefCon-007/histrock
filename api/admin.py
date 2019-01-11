from django.contrib import admin
from .models import StockHistoricData, Stock
from import_export.admin import ImportExportModelAdmin

class StockHistoricDataAdmin(ImportExportModelAdmin) :
    list_display = []
    # list_filter = ["attendanceStatus", "event"]
    for columnName in StockHistoricData._meta.fields :
        list_display.append(columnName.get_attname_column()[0])

class StockAdmin(ImportExportModelAdmin) :
    list_display = []
    # list_filter = ["attendanceStatus", "event"]
    for columnName in Stock._meta.fields :
        list_display.append(columnName.get_attname_column()[0])

admin.site.register(Stock, StockAdmin)
admin.site.register(StockHistoricData, StockHistoricDataAdmin)

# Register your models here.

from django.contrib import admin
from .models import Monitor

# Register your models here.

class MonitorAdmin(admin.ModelAdmin):
    list_display = ('memory_used','memory_spare','cpu_load_5m','cpu_load_10m','cpu_load_15m')
    list_display_links = ('cpu_load_5m','cpu_load_10m')
    list_editable =('memory_used','memory_spare')
    search_fields = ('memory_used', 'memory_spare',)
    list_per_page = 10


admin.site.register(Monitor,MonitorAdmin)
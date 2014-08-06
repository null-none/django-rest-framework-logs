from django.contrib import admin

from .models import Logger


class LoggerAdmin(admin.ModelAdmin):
    list_display = ('params', 'method_class',
                    'query', 'result', 'status', 'created')
    search_fields = ['method_class', 'query', 'result']
    list_filter = ['status']
    date_hierarchy = 'created'

admin.site.register(Logger, LoggerAdmin)

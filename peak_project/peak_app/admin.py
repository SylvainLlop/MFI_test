from django.contrib import admin

from .models import Peak


class PeakAdmin(admin.ModelAdmin):
    list_display = ('name', 'altitude', 'lat', 'lon')
    list_filter = ('name',)
    ordering = ('name', '-altitude')
    search_fields = ('name',)


admin.site.register(Peak, PeakAdmin)

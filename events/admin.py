from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location', 'created_by')
    list_filter = ('date',)
    search_fields = ('title', 'description', 'location')

from django.contrib import admin
from .models import Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'material_type', 'created_at', 'created_by')
    list_filter = ('material_type', 'created_at')
    search_fields = ('title', 'description')

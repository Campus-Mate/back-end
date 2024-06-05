from django.contrib import admin
from .models import IDRecord

@admin.register(IDRecord)
class IDRecordAdmin(admin.ModelAdmin):
    list_display = ('id_value', 'title', 'content', 'category', 'created_at')

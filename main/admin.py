from django.contrib import admin

from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('user__username', 'description')


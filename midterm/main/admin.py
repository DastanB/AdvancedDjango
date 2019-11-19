from django.contrib import admin
from main import models
# Register your models here.
@admin.register(models.Product)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'price', 'product_type', 'size', 'existence')
    
@admin.register(models.Service)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'price', 'service_type', 'aproximate_duration')

from django.contrib import admin
from .models import HealthData, HealthTip

@admin.register(HealthData)
class HealthDataAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'metric_type', 'value', 'timestamp')

@admin.register(HealthTip)
class HealthTipAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'tip', 'timestamp')

from django.contrib import admin
from Subscription.models import Subscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'plan_type', 'start_date', 'end_date')
    search_fields = ('user__username', 'plan_type')
    list_filter = ('plan_type', 'start_date', 'end_date')
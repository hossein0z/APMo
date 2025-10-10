from rest_framework import permissions
from .models import Subscription
from datetime import date

class IsSubscriptionActive(permissions.BasePermission):
    """
    اجازه دسترسی فقط به کاربران دارای اشتراک فعال.
    """

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        # بررسی اشتراک فعال کاربر
        active_subscriptions = Subscription.objects.filter(user=user, end_date__gte=date.today())
        return active_subscriptions.exists()

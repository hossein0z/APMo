from rest_framework import serializers
from .models import Subscription, Payment

class SubscriptionSerializer(serializers.ModelSerializer):
    is_active = serializers.ReadOnlyField()

    class Meta:
        model = Subscription
        fields = ['id', 'user', 'start_date', 'end_date', 'plan_type', 'is_active']
        read_only_fields = ['start_date', 'user']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'amount', 'paid_at', 'subscription', 'status']
        read_only_fields = ['paid_at', 'user']

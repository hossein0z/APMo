from rest_framework import serializers
from .models import WatchHistory
from Subscription.models import Payment

class WatchHistorySerializer(serializers.ModelSerializer):
    video_title = serializers.ReadOnlyField(source='video.title')

    class Meta:
        model = WatchHistory
        fields = ['id', 'video', 'video_title', 'watched_at']

class PaymentHistorySerializer(serializers.ModelSerializer):
    subscription_plan = serializers.ReadOnlyField(source='subscription.plan_type')

    class Meta:
        model = Payment
        fields = ['id', 'amount', 'paid_at', 'status', 'subscription', 'subscription_plan']

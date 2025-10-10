from rest_framework import generics, permissions
from .models import Subscription
from .serializers import SubscriptionSerializer, PaymentSerializer
from datetime import timedelta, date
from django.utils import timezone

class SubscriptionCreateView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        plan = serializer.validated_data.get('plan_type')
        start_date = timezone.now()
        
        if plan == 'basic':
            end_date = start_date + timedelta(days=90)  
        elif plan == 'medium':
            end_date = start_date + timedelta(days=180)  
        elif plan == 'premium':
            end_date = start_date + timedelta(days=395)  
        else:
            end_date = start_date

        serializer.save(user=self.request.user, start_date=start_date, end_date=end_date)

class SubscriptionListView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)


class PaymentCreateView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


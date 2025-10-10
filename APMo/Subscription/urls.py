from django.urls import path
from .views import SubscriptionCreateView, SubscriptionListView, PaymentCreateView

urlpatterns = [
    path('subscriptions/', SubscriptionListView.as_view(), name='subscription-list'),
    path('subscriptions/create/', SubscriptionCreateView.as_view(), name='subscription-create'),
    path('payments/create/', PaymentCreateView.as_view(), name='payment-create'),
]

from django.urls import path
from .views import WatchHistoryListView, PaymentHistoryListView, VideoWatchView

urlpatterns = [
    path('history/watch/', WatchHistoryListView.as_view(), name='watch-history'),
    path('history/payments/', PaymentHistoryListView.as_view(), name='payment-history'),
    path('videos/<int:video_id>/watch/', VideoWatchView.as_view(), name='video-watch'),
]

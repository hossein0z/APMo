from rest_framework import generics, permissions
from Subscription.models import Payment
from WatchHistory.serializers import WatchHistorySerializer , PaymentHistorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Video, WatchHistory

class WatchHistoryListView(generics.ListAPIView):
    serializer_class = WatchHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WatchHistory.objects.filter(user=self.request.user).order_by('-watched_at')


class PaymentHistoryListView(generics.ListAPIView):
    serializer_class = PaymentHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user).order_by('-paid_at')




class VideoWatchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, video_id):
        try:
            video = Video.objects.get(id=video_id)
        except Video.DoesNotExist:
            return Response({'detail': 'Video not found.'}, status=status.HTTP_404_NOT_FOUND)


        WatchHistory.objects.create(user=request.user, video=video)

        return Response({'detail': 'Watch history recorded.'})

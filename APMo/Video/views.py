from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Video
from .serializers import VideoSerializer
from Subscription.services import IsSubscriptionActive

class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddVideoByUrlView(generics.CreateAPIView):
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description', ''),
            'video_url': request.data.get('video_url'),
            'rating' : request.data.get('rating'),
        }

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VideoDetailView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated, IsSubscriptionActive]

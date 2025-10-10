from django.urls import path
from Video.views import *

urlpatterns = [
    path('', VideoListView.as_view(), name='video-list'),
    path('watchvideo/<int:pk>/', VideoDetailView.as_view() ),
    path('videos/add-url/', AddVideoByUrlView.as_view(), name='add-video-by-url'),
]

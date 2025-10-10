from django.db import models
from User.models import Abs_User
from Video.models import Video

class WatchHistory(models.Model):
    user = models.ForeignKey(Abs_User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    watched_at = models.DateTimeField(auto_now_add=True)


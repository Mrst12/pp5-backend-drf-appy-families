'''views file for likes for achievements'''
from rest_framework import generics, permissions
from p5_drf_api.permissions import IsOwnerOrReadOnly
from like_achievements.models import AchievementLikes
from like_achievements.serializers import AchievementLikesSerializer


class AchievementLikesList(generics.ListCreateAPIView):
    '''list likes or create a like if logged in'''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AchievementLikesSerializer
    queryset = AchievementLikes.objects.all()

    def perform_create(self, serializer):
        '''create like'''
        serializer.save(owner=self.request.user)

'''views file for comments for achievements page'''
from rest_framework import generics, permissions
from p5_drf_api.permissions import IsOwnerOrReadOnly
from .models import AchievementsComment
from .serializers import (
    AchievementsCommentSerializer, AchievementsCommentDetailSerializer
)


class AchievementsCommentList(generics.ListCreateAPIView):
    '''List or create comments if logged in'''
    serializer_class = AchievementsCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = AchievementsComment.objects.all()

    def perform_create(self, serializer):
        '''make sure comments associated with user'''
        serializer.save(owner=self.request.user)

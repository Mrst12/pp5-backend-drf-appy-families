'''views file for achievements app'''
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from p5_drf_api.permissions import IsOwnerOrReadOnly
from .models import Achievements
from .serializers import AchievementSerializer


class AchievementList(generics.ListCreateAPIView):
    '''list achievements and create achievement if logged in'''
    serializer_class = AchievementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Achievements.objects.annotate(
        achievements_comments_count=Count(
            'achievementscomment', distinct=True
        ),
        achievements_likes_count=Count('like_achievements', distinct=True),
    ).order_by('-date_created')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'like_achievements__owner__profile',
        'owner__profile',
        'owner__followed__owner__profile',
    ]
    search_fields = [
        'owner__username',
        'content',
        'title',
    ]
    ordering_fields = [
        'achievements_comments_count',
        'achievements_likes_count',
    ]

    def perform_create(self, serializer):
        '''associate achievement with logged in user'''
        serializer.save(owner=self.request.user)


class AchievementDetail(generics.RetrieveUpdateDestroyAPIView):
    '''retrieve, edit,or delete if owned by user'''
    serializer_class = AchievementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Achievements.objects.annotate(
        achievements_comments_count=Count(
            'achievementscomment', distinct=True
        ),
        achievements_likes_count=Count('like_achievements', distinct=True),
    ).order_by('-date_created')

''' views for profile app '''
from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from p5_drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


# class taken from DRF_API walkthrough
class ProfileList(generics.ListAPIView):
    '''profile list '''
    queryset = Profile.objects.annotate(
        memo_posts_count=Count('owner__memo_posts', distinct=True),
        achievements_posts_count=Count('owner__achievements', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_on')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile',
    ]
    ordering_fields = [
        'memo_posts_count',
        'achievements_posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_on',
        'owner__followed__created_on',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    ''' fetching or update if profile owner '''
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        memo_posts_count=Count('owner__memo_posts', distinct=True),
        achievements_posts_count=Count('owner__achievements', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_on')

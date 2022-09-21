''' views file for memo posts '''
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from p5_drf_api.permissions import IsOwnerOrReadOnly
from .models import Memo
from .serializers import MemoSerializer


# class taken from DRF_API walkthrough with modifications
class MemoList(generics.ListCreateAPIView):
    ''' create memo post list view '''
    serializer_class = MemoSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Memo.objects.all()
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'like_memo__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'content',
        'For',
    ]

    def perform_create(self, serializer):
        '''make sure user associated with memo post'''
        serializer.save(owner=self.request.user)


# Class taken from DRF_API walkthrough with modifications
class MemoDetail(generics.RetrieveUpdateDestroyAPIView):
    ''' Retrieve, update or delete if owner  '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MemoSerializer
    queryset = Memo.objects.all()

'''views for comments for memo posts'''
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from p5_drf_api.permissions import IsOwnerOrReadOnly
from .models import MemoComment
from .serializers import MemoCommentSerializer, MemoCommentDetailSerializer


# code taken from DRF_API walkthrough with modifications
class MemoCommentList(generics.ListCreateAPIView):
    '''list view for memo comments'''
    serializer_class = MemoCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = MemoComment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['memo_post']

    def perform_create(self, serializer):
        '''make sure comments associated with user'''
        serializer.save(owner=self.request.user)


# class taken from DRF_API walkthrough with modifications
class MemoCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    '''show details of comments'''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MemoCommentDetailSerializer
    queryset = MemoComment.objects.all()

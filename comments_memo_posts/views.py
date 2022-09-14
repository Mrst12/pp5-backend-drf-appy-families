'''views for comments for memo posts'''
from rest_framework import generics, permissions
from p5_drf_api.permissions import IsOwnerOrReadOnly
from .models import MemoComment
from .serializers import MemoCommentSerializer, MemoCommentDetailSerializer


# code taken from DRF_API walkthrough with modifications
class MemoCommentList(generics.ListCreateAPIView):
    '''list view for memo comments'''
    serializer_class = MemoCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = MemoComment.objects.all()

    def perform_create(self, serializer):
        '''make sure comments associated with user'''
        serializer.save(owner=self.request.user)

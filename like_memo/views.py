'''views for memo posts likes app'''
from rest_framework import generics, permissions
from p5_drf_api.permissions import IsOwnerOrReadOnly
from like_memo.models import MemoLikes
from like_memo.serializers import MemoLikesSerializer


# Class taken from DRF_API walkthrough with modifications
class MemoLikesList(generics.ListCreateAPIView):
    '''list likes or create a like if logged in'''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MemoLikesSerializer
    queryset = MemoLikes.objects.all()

    def perform_create(self, serializer):
        '''create like'''
        serializer.save(owner=self.request.user)


# class taken from DRF_API walkthrough with modifications
class MemoLikesDetail(generics.RetrieveDestroyAPIView):
    '''retrieve and delete a like if owned by user'''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MemoLikesSerializer
    queryset = MemoLikes.objects.all()

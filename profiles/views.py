''' views for profile app '''
from rest_framework import generics
from p5_drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


# class taken from DRF_API walkthrough
class ProfileList(generics.ListAPIView):
    '''profile list '''
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    ''' fetching or update if profile owner '''
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()

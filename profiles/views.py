''' views for profile app '''
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


# class taken from DRF_API walkthrough


class ProfileList(APIView):
    ''' create profile list '''
    def get(self, request):
        '''get method'''
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

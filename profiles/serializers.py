''' serializers for profile app '''
from rest_framework import serializers
from .models import Profile


# class taken from DRF-APi walkthrough with modifications
class ProfileSerializer(serializers.ModelSerializer):
    '''profile serializer class'''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        '''fields we want to display'''
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'name', 'bio',
            'image',
        ]

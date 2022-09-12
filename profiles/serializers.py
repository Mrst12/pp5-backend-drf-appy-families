''' serializers for profile app '''
from rest_framework import serializers
from .models import Profile


# class taken from DRF-APi walkthrough with modifications
class ProfileSerializer(serializers.ModelSerializer):
    '''profile serializer class'''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        ''' check user is owner '''
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        '''fields we want to display'''
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'name', 'bio',
            'image', 'is_owner',
        ]

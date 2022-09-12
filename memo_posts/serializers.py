'''  serializers for memo posts app'''
from rest_framework import serializers
from .models import Memo


# class taken for DRF_API walkthrough
class MemoSerializer(serializers.ModelSerializer):
    '''Memo posts serializer class'''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        '''check user is owner'''
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        ''' fields we want to display '''
        model = Memo
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_on', 'content',
        ]

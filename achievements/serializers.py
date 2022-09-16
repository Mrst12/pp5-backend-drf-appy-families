'''serailizers for achievements app'''
from rest_framework import serializers
from achievements.models import Achievements


class AchievementSerializer(serializers.ModelSerializer):
    '''serializer class for main serializer app'''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        '''check user is owner'''
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        '''fields we want to display'''
        model = Achievements
        fields = [
            'id', 'owner', 'date_created', 'title', 'content',
            'image', 'is_owner', 'profile_id', 'profile_image',
        ]

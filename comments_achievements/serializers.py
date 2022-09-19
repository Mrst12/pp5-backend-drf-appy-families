'''serializer file for comments for the achievements page'''
from rest_framework import serializers
from .models import AchievementsComment


class AchievementsCommentSerializer(serializers.ModelSerializer):
    '''serailaizer for achievements comments model'''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        '''check owner is user'''
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        '''fields to be displayed'''
        model = AchievementsComment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'achievement_post', 'created_on', 'content',
        ]


class AchievementsCommentDetailSerializer(AchievementsCommentSerializer):
    '''serializer for achievements comments used in detail view'''
    achievement_post = serializers.ReadOnlyField(source='achievement_post.id')

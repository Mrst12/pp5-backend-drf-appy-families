'''serializers file for the likes for achievements page'''
from rest_framework import serializers
from like_achievements.models import AchievementLikes


class AchievementLikesSerializer(serializers.ModelSerializer):
    '''serializer class for likes for achievements'''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        '''fields to display'''
        model = AchievementLikes
        fields = [
            'id', 'created_on', 'owner', 'achievement_post'
        ]

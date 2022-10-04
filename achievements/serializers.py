'''serailizers for achievements app'''
from rest_framework import serializers
from like_achievements.models import AchievementLikes
from achievements.models import Achievements


class AchievementSerializer(serializers.ModelSerializer):
    '''serializer class for main serializer app'''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    achievements_comments_count = serializers.ReadOnlyField()
    achievements_likes_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        '''make sure uploaded image does not exceed size'''
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image larger than 2MB! Please reduce'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px Please reduce'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px plese reduce'
            )
        return value

    def get_is_owner(self, obj):
        '''check user is owner'''
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        '''owner can unlike the achievement'''
        user = self.context['request'].user
        if user.is_authenticated:
            like = AchievementLikes.objects.filter(
                owner=user, achievement_post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        '''fields we want to display'''
        model = Achievements
        fields = [
            'id', 'owner', 'date_created', 'title', 'content',
            'image', 'is_owner', 'profile_id', 'profile_image',
            'like_id', 'achievement_comments_count', 'achievement_likes_count',
        ]

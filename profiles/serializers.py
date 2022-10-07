''' serializers for profile app '''
from rest_framework import serializers
from followers.models import Follower
from .models import Profile


# class taken from DRF-APi walkthrough with modifications
class ProfileSerializer(serializers.ModelSerializer):
    '''profile serializer class'''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    memo_posts_count = serializers.ReadOnlyField()
    achievements_posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        ''' check user is owner '''
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        '''return following count'''
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        '''fields we want to display'''
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'name', 'bio',
            'image', 'is_owner', 'following_id',
            'memo_posts_count', 'achievements_posts_count',
            'followers_count', 'following_count',
        ]

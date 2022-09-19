'''serializer for the memo_posts comments'''
from rest_framework import serializers
from .models import MemoComment


# class taken from DRF_API walkthrough with modifications for this project
class MemoCommentSerializer(serializers.ModelSerializer):
    '''serializer for memo posts comment model'''
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
        model = MemoComment
        fields = [
            'id', 'owner', 'memo_post', 'created_on', 'content',
            'is_owner', 'profile_id', 'profile_image',
        ]


# class taken from DRF_API walkthrough
class MemoCommentDetailSerializer(MemoCommentSerializer):
    '''serializer for the comment model used in the detail view'''
    memo_post = serializers.ReadOnlyField(source='memo_post.id')

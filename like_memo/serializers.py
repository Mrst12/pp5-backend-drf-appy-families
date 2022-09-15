'''serializer page for likes in the memo posts'''
from django.db import IntegrityError
from rest_framework import serializers
from like_memo.models import MemoLikes


# class taken from steps of DRF_API challenge in walkthrough
class MemoLikesSerializer(serializers.ModelSerializer):
    '''serializer for the like model for memo posts'''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        '''class for fields to show'''
        Model = MemoLikes
        fields = [
            'id', 'created_on', 'owner', 'memo_post'
        ]

    def create(self, validated_data):
        '''stopping integrity errors'''
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })

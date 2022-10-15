'''serializer for todo page'''
from rest_framework import serializers
from to_do.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    '''serializer for the Todo app'''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        '''check user is owner'''
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        '''which fields to display'''
        model = Todo
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_on', 'task_title', 'due_date', 'urgent', 'status',
            'content',
        ]

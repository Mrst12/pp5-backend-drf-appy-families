'''permissions so only logged in can edit'''
from rest_framework import permissions


# class taken for DRF-API walkthrough
class IsOwnerOrReadOnly(permissions.BasePermission):
    ''' make sure the user can edit only '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

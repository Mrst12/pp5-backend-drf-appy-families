''' views file for memo posts '''
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from p5_drf_api.permissions import IsOwnerOrReadOnly
from .models import Memo
from .serializers import MemoSerializer


# class taken from DRF_API walkthrough with modifications
class MemoList(APIView):
    ''' create memo post list view '''
    serializer_class = MemoSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        ''' get the memo posts to the view'''
        memo_post = Memo.objects.all()
        serializer = MemoSerializer(
            memo_post, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        '''allow users to create memo posts'''
        serializer = MemoSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


# Class taken from DRF_API walkthrough with modifications
class MemoDetail(APIView):
    ''' class to show the memo's  '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MemoSerializer

    def get_object(self, pk):
        '''get the memo'''
        try:
            memo = Memo.objects.get(pk=pk)
            self.check_object_permissions(self.request, memo)
            return memo
        except Memo.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        '''memo posts'''
        memo = self.get_object(pk)
        serializer = MemoSerializer(
            memo, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        '''allow update of memo'''
        memo = self.get_object(pk)
        serializer = MemoSerializer(
            memo, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        '''allow for deletion of memo's'''
        memo = self.get_object(pk)
        memo.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

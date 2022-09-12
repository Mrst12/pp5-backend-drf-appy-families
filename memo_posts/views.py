''' views file for memo posts '''
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
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

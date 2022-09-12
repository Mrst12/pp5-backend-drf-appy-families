''' views file for memo posts '''
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Memo
from .serializers import MemoSerializer


# class taken from DRF_API walkthrough with modifications
class MemoList(APIView):
    ''' create memo post list view '''
    def get(self, request):
        ''' get the memo posts to the view'''
        memo_post = Memo.objects.all()
        serializer = MemoSerializer(
            memo_post, many=True, context={'request': request}
        )
        return Response(serializer.data)

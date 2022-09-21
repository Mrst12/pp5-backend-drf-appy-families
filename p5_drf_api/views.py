'''views file for main drf project'''
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    '''main route'''
    return Response({
        "message": "Welcome to the Appy Families drf API!!"
    })

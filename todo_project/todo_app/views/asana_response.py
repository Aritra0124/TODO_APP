from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..views.asana_connection import test
@api_view(['GET'])
def test_response(request):
    if request.method == 'GET':
        data = test()
        return Response(data, status= status.HTTP_200_OK)
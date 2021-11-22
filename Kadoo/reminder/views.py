from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import *

@api_view(['POST'])
def reminder(request):
    data = EventSerializer(data=request.data)
    if data.is_valid():
        return Response(data.data)
    
    return Response(data.errors)
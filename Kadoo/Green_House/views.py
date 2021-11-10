from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import myPlant
from .serializers import myPlantSerializer

@api_view(['GET'])
def allOfMyPlant(request):
    if request.user.is_anonymous:
      return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
    _user = request.user
    myPlants = myPlant.objects.filter(user = _user)
    serializer = myPlantSerializer(myPlants, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPlantToMyGreenHouse(request):
    serializer = myPlantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updatePlantInMyGreenHouse(request, pk):
    _myPlant = get_object_or_404(myPlant, id=pk)
    serializer = myPlantSerializer(instance =_myPlant, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
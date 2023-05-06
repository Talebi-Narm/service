from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import UserPlant
from .serializers import UserPlantSerializer


class UserPlantListAPIView(ListCreateAPIView):
    swagger_tags = ('green house',)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserPlantSerializer

    def get_queryset(self):
        return UserPlant.objects.filter(user=self.request.user, is_deleted=False)


class UserPlantDetailAPIView(RetrieveUpdateDestroyAPIView):
    swagger_tags = ('green house',)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserPlantSerializer

    def get_queryset(self):
        return UserPlant.objects.filter(user=self.request.user, is_deleted=False)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

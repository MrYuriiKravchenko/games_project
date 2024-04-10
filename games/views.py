from rest_framework import generics, viewsets

from .models import Games
from .serializers import GamesSerializer


class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
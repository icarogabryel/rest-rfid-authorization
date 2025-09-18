from rest_framework import generics

from .models import Card
from .serializers import CardCreateSerializer, CardDetailSerializer


class CardCreateView(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardCreateSerializer


class CardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardDetailSerializer
    lookup_field = 'id'

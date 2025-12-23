from django.shortcuts import render
from rest_framework import viewsets
from .models import Board, Block
from .serializers import BoardSerializer, BlockSerializer

# Create your views here.
class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
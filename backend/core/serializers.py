from core.models import Board, Block
from rest_framework import serializers

#Não passar o
class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ["id", "text", "x_position", "y_position", "board"]

class BoardSerializer(serializers.ModelSerializer):
    blocks = BlockSerializer(many=True, read_only=True)
    class Meta:
        model = Board
        fields = ["id", "title", "blocks"]


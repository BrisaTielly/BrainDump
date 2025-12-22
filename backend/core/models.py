from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Board(models.Model):
    #Cria o Id automaticamente...
    title = models.CharField(max_length=100,null=False, blank=False )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')

class Block(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='blocks')
    text = models.TextField()
    x_position = models.FloatField()
    y_position = models.FloatField()

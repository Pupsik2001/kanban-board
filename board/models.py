from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Column(models.Model):
    name = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    position = models.IntegerField()

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    position = models.IntegerField()
    

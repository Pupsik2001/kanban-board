from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    board = models.CharField(max_length=100)


    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.board

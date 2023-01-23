from django.shortcuts import render
from .models import Board


def board_list(request):
	boards = Board.objects.all()
	return render(request, 'board/board_list.html', {'boards': boards})
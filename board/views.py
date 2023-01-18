from django.shortcuts import render
from django.http import HttpResponse
from board.models import Board
from board.forms import BoardForm
from django.contrib import message
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def board(request):
	if request.method = 'POST':
		form = BoardForm(request.POST or None)
		if form.is_valid():
			instance.manage = form.save(commit=False)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Board
from .forms import BoardForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



@login_required
def board_list(request):
	if request.method == 'POST':
		form = BoardForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.manage = request.user 
			instance.save()
		messages.success(request, ('add new card'))
		return redirect('boards')
	else:
		all_cards = Board.objects.filter(manage=request.user)
		paginator = Paginator(all_cards, 20)
		page = request.GET.get('pg')
		all_cards = paginator.get_page(page)

		return render(request, 'board/board_list.html', {'boards': boards})

@login_required
def delete_card(request, card_id):
	card = Board.objects.get(pk=card_id)
	if card.manage == request.user:
		card.delete()
	else:
		messages.error(request, ('Access Restricted, Your are not allowed.'))

	return redirect('boards')

@login_required
def edir_card(request, card_id):
	if request.method == 'POST':
		card = Board.objects.get(pk=card_id)
		if card.manage == request.user:
			card.done = True
			card.save()
		else:
			messages.error(request, ('Access Restricted, You are not allowed.'))

		return redirect('boards')

@login_required
def pending_card(request, card_id):
	card = Board.objects.get(pk=card_id)
	card.done = False
	card.save()

	return redirect('boards')
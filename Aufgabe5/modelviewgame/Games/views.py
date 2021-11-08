from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from .forms import GameForm
from .models import Game


def game_list(request):
    all_games = Game.objects.all()
    context = {'all_the_games': all_games}
    return render(request, 'game-list.html', context)


def game_detail(request, **kwargs):
    game_id = kwargs['pk']
    detailed_game = Game.objects.get(id=game_id)
    context = {'that_game': detailed_game}
    return render(request, 'game-detail.html', context)


def game_create(request):
    if request.method == 'POST':
        create_game_form = GameForm(request.POST)
        create_game_form.instance.user = request.user
        if create_game_form.is_valid():
            create_game_form.save()
        else:
            pass
        return redirect('game-list')

    else: 
        create_game_form = GameForm()
        context = {'form': create_game_form}
        return render(request, 'game-create.html', context)


def game_delete(request, **kwargs):
    game_id = kwargs['pk']
    Game.objects.filter(id=game_id).delete()
    return redirect('game-list')
import re
from django.forms import ImageField
from django.shortcuts import redirect, render

from games.form import GameForm
from games.models import Games

# Create your views here.


def games_view(request):
    if(request.method == "POST"):
        page = int(request.POST['page'])
        if('prev' in request.POST):
            page = page-1
        if ('next' in request.POST):
            page = page+1
        tempOffSet = page - 1
        offset = tempOffSet*4
        print(offset)
    else:
        offset = 0
        page = 1
    games = Games.objects.raw(
        "select * from games limit 4 offset % s", [offset])
    pageItem = len(games)
    return render(request, "games/view.html", {'games': games, 'page': page, 'pageItem': pageItem})


def games_add(request):
    if request.method == "POST":
        form = GameForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                return redirect("/games/games_view")
            except:
                print("Failed")
        else:
            form = GameForm()
            print("invalid")

    return render(request, 'games/create.html')


def games_edit(request, p_id):
    try:
        games = Games.objects.get(id=p_id)
        return render(request, "games/edit.html", {'games': games})
    except:
        print("No Data Found")
    return redirect("games/games_view")


def games_update(request, p_id):
    games = Games.objects.get(id=p_id)
    form = GameForm(request.POST, instance=games)
    if form.is_valid():
        try:
            form. save()
            return redirect("/games/games_view")
        except:
            print("validation failed")
    return render(request, "games/edit.html", {'games': games})


def games_delete(request, p_id):
    try:
        games = Games.objects.get(id=p_id)
        games.delete()
    except:
        print("cannot perform")
    return redirect("/games/games_view")


def games_all(request):
    games = Games.objects.all()
    return render(request, "allgames.html",{'games':games})


def games_rpg(request):
    games = Games.objects.filter(type='Role Playing Game')
    return render(request, "rpg.html", {'games': games})

def games_battle(request):
    games = Games.objects.filter(type='Battle Royale')
    return render(request, "battle.html", {'games': games})

def games_board(request):
    games = Games.objects.filter(type='Board Games')
    return render(request, "board.html", {'games': games})

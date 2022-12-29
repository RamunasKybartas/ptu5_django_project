from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Player, Staff, Arena, Sponsor, Team
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

def index(request):
    num_teams = Team.objects.all().count()
    num_players = Player.objects.all().count()
    num_centers = Player.objects.filter(position='C').count()
    num_pf = Player.objects.filter(position='PF').count()
    num_sf = Player.objects.filter(position='SF').count()
    num_sg = Player.objects.filter(position='SG').count()
    num_pg = Player.objects.filter(position='PG').count()
    num_staff = Staff.objects.count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'Total_teams' : num_teams,
        'Total_players': num_players,
        'Total_centers' : num_centers,
        'Total_power_forwards' : num_pf,
        'Total_small_forwards' : num_sf,
        'Total_shooting_guards' : num_sg,
        'Total_point_guards' : num_pg,
        'Total_staff_members' : num_staff,
        'num_visits' : num_visits,
    }
    return render(request, 'basketball/index.html', context=context)

def teams(request):
    paginator = Paginator(Team.objects.all(), 14)
    page_number = request.GET.get('page')
    paged_teams =  paginator.get_page(page_number)
    context = {
        'teams' : paged_teams
    }

    return render(request, 'basketball/teams.html', context=context)

def team(request, team_id):
    single_team = get_object_or_404(Team, pk=team_id)
    return render(request, 'basketball/team.html', {'team': single_team})


class PlayerListView(generic.ListView):
    model = Player
    template_name = 'basketball/player_list.html'


class PlayerDetailView(generic.DetailView):
    model = Player
    template_name = 'basketball/player_detail.html'


def sponsors(request):
    sponsors = Sponsor.objects.all()
    context = {
        'Sponsors' : sponsors
    }
    print(sponsors)
    return render(request, 'basketball/sponsors.html', context=context)


def search(request):    
    query = request.GET.get('query')
    search_results1 = Player.objects.filter(Q(name__icontains=query) | Q(surname__icontains=query))
    # search_results2 = Staff.objects.filter(Q(name__icontains=query) | Q(surname__icontains=query))
    # search_results = search_results1 & search_results2
    return render(request, 'basketball/search.html', {'players': search_results1, 'query' : query })


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username {username} is taken!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'User with {email} is already registered!')
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'User {username} registered!')
                    return redirect('login')
        else:
            messages.error(request, "Passwords don't match!")
            return redirect('register')
    return render(request, 'registration/register.html')
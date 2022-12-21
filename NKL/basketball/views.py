from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Player, Staff, Arena, Sponsor, Team
from django.views import generic

def index(request):
    num_teams = Team.objects.all().count()
    num_players = Player.objects.all().count()
    num_centers = Player.objects.filter(position='C').count()
    num_pf = Player.objects.filter(position='PF').count()
    num_sf = Player.objects.filter(position='SF').count()
    num_sg = Player.objects.filter(position='SG').count()
    num_pg = Player.objects.filter(position='PG').count()
    num_staff = Staff.objects.count()

    context = {
        'Total_teams' : num_teams,
        'Total_ players': num_players,
        'Total_centers' : num_centers,
        'Total_power_forwards' : num_pf,
        'Total_small_forwards' : num_sf,
        'Total_shooting_guards' : num_sg,
        'Total_point_guards' : num_pg,
        'Total_staff_members' : num_staff
    }
    return render(request, 'basketball/index.html', context=context)

def teams(request):
    teams = Team.objects.all()
    context =  {
        'Teams' : teams
    }
    print(teams)
    return render(request, 'basketball/teams.html', context=context)

def team(request, team_id):
    single_team = get_object_or_404(Team, pk=team_id)
    return render(request, 'basketball/team.html', {'team': single_team})


class PlayerListView(generic.ListView):
    model = Player
    template_name = 'player_list.html'


class PlayerDetailView(generic.DetailView):
    model = Player
    template_name = 'player_detail.html'


def sponsors(request):
    sponsors = Sponsor.objects.all()
    context = {
        'Sponsors' : sponsors
    }
    print(sponsors)
    return render(request, 'basketball/sponsors.html', context=context)




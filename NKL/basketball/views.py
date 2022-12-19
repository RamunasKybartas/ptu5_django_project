from django.http import HttpResponse
from django.shortcuts import render
from .models import Player, Staff, Arena, Sponsor, Team

def index(request):
    num_teams = Team.objects.all().count()
    num_players = Player.objects.count()
    num_centers = Player.objects.filter(position='C').count()
    num_pf = Player.objects.filter(position='PF').count()
    num_sf = Player.objects.filter(position='SF').count()
    num_sg = Player.objects.filter(position='SG').count()
    num_pg = Player.objects.filter(position='PG').count()
    num_staff = Staff.objects.all().count()

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
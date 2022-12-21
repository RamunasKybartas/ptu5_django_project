from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teams/', views.teams, name='teams'),
    path('teams/<int:team_id>', views.team, name='team'),
    path('players/', views.PlayerListView.as_view(), name='players'),
    path('players/<int:pk>', views.PlayerDetailView.as_view(), name='player_detail'),
    path('sponsors/', views.sponsors, name='sponsors'),
]
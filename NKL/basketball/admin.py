from django.contrib import admin
from .models import Player, Staff, Arena, Team, Sponsor

# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'team')
    search_fields = ('name', 'surname')
    list_editable = ('team',)


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'team')
    search_fields = ('name', 'surname')
    list_editable = ('team',)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_sponsors', 'display_arenas')

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'team')

class ArenaAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'capacity')

admin.site.register(Player, PlayerAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Arena, ArenaAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Sponsor, SponsorAdmin)
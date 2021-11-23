from django.contrib import admin

from .models import Team, Member

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'logo',)
    prepopulated_fields = {'slug': ('team_name',)}

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name','team', 'description','avatar')
    prepopulated_fields = {'slug': ('name',)}
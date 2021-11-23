from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, detail
from .models import Team, Member


def teamView(request):
    team_ = Team.objects.all()
    context = {
        'team': team_,
    }
    return render(request, 'team/team.html', context)

def teamDetail(request, pk):
    detail = Team.objects.get(pk=pk)
    member = Member.objects.all().filter(team=pk)
    team_list = Team.objects.all()
    print(pk)
    context = {
        'pk': pk,
        'detail': detail,
        'member': member,
        'team_list': team_list
    }
    return render(request, 'team/team_detail.html', context)

def memberDetail(request, pk):
    detail = Member.objects.all().filter(name=pk)
    team_list = Team.objects.all()
    context = {
        'detail': detail,
        'team_list': team_list
    }
    return render(request, 'member/member_detail.html', context)
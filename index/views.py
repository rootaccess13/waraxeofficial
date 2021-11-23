from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required as lr
from django.contrib.auth.models import User
from api.models import UpcomingMatche, BetModel, TeamModel
from django.db.models import Avg, Sum
from currency_symbols import CurrencySymbols
from api.get_username import get_username
from team.models import Team
import uuid
# Create your views here


@lr(login_url='/accounts/signin/')

def index(request):
    if request.user.is_authenticated:
        user = get_username()
        id = request.user.id
        upcoming = UpcomingMatche.objects.all()
        bethistory = BetModel.objects.filter(better=request.user).order_by('-id')
        ave = BetModel.objects.filter(better = user.user).aggregate(Sum('amount'))
        income =  BetModel.objects.filter(status = "Win",better=user.user).aggregate(Sum('amount'))
        # percentage = 5 / 100 * income['amount__sum']
        # print(percentage)
        mod = BetModel.objects.all()
        symbol = CurrencySymbols.get_symbol('PHP')
        team_list = Team.objects.all()
    context = {
        'id' : id,
        'upcoming': upcoming,
        'history': bethistory,
        'average': ave['amount__sum'],
        'income': income['amount__sum'],
        'symbol': symbol,
        'team_list': team_list
    }

    return render(request, 'index/index.html', context)

#Create Class Based View for Betting using List View
#import necessary libraries
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from api.models import BetModel, UpcomingMatche
# from django.db.models import Avg, Sum
# from django.shortcuts import render, redirect

# class BetListView(LoginRequiredMixin, ListView):
#     model = BetModel
#     template_name = 'bet/bet_list.html'
#     context_object_name = 'bet_list'
#     ordering = ['-id']
#     paginate_by = 10

#     def get_queryset(self):
#         return BetModel.objects.filter(better=self.request.user)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['bet_list'] = BetModel.objects.filter(better=self.request.user)
#         context['upcoming'] = UpcomingMatche.objects.all()
#         context['symbol'] = CurrencySymbols.get_symbol('PHP')
#         return context
    

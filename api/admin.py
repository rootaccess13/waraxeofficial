from django.contrib import admin
from . models import *

@admin.register(BetModel)
class BetModelAdmin(admin.ModelAdmin):
    list_display = ('id','better', 'matches','pick', 'status', 'amount', 'time',)
    list_filter = ("matches", )
admin.site.register(TeamModel)
admin.site.register(UpcomingMatche)
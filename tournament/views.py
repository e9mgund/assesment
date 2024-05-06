from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from .models import Team , TeamMatch , Match
from django.views import generic


class ListView(generic.ListView):
    template_name = "tournament/team_list.html"
    context_object_name = "team_list"

    def get_queryset(self) -> QuerySet[Any]:
        return Team.objects.all()

class DetailView(generic.DetailView):
    template_name = "tournament/team_view.html"
    model = "Team"
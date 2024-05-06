from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from .models import Team , TeamMatch , Match
from django.views import generic


class ListView(generic.ListView):
    template_name = "templates/team_list.html"
    context_object_name = "team_list"

    def get_queryset(self) -> QuerySet[Any]:
        result = []

        for i in Team.objects.all():
            result.append({"team" : i.country,"matches" : i.matches_played(),"won" : i.matches_won(),"lost" : i.matches_lost(),"points" : i.matches_played() - i.matches_lost() })
        return result

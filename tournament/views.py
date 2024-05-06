from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TeamMatchForm
from .models import Team, TeamMatch, Match
from django.views import generic
from rest_framework import viewsets
from .serializers import TeamSerializer


class ListView(generic.ListView):
    template_name = "tournament/team_list.html"
    context_object_name = "team_list"

    def get_queryset(self) -> QuerySet[Any]:
        return Team.objects.all()


class DetailView(generic.DetailView):
    template_name = "tournament/team_view.html"
    model = Team


class NewDetailView(generic.DetailView):
    template_name = "tournament/team_view_form.html"
    model = TeamMatch

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

def fill(request):
    form = TeamMatchForm

    if request.method == "POST":
        form = TeamMatchForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "tournament/match_form.html", context)

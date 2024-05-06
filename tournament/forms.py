from django.forms import ModelForm
from .models import Match, TeamMatch


class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = "__all__"


class TeamMatchForm(ModelForm):
    class Meta:
        model = TeamMatch
        fields = "__all__"

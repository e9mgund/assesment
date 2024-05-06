from django.db import models

# Create your models here.
class Team(models.Model):
    country = models.CharField(max_length=3, unique=True)
    matches = models.IntegerField()
    won = models.IntegerField()
    lost = models.IntegerField()

    def matches_played(self) -> int:
        return self.matches

    def matches_won(self) -> int:
        return self.won

    def matches_lost(self) -> int:
        return self.lost

    def __str__(self):
        return self.country

class Match(models.Model):
    date = models.DateField()

class TeamMatch(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_matches')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='team_matches')
    batting_score = models.IntegerField()
    batting_wickets = models.IntegerField()
    batting_overs = models.IntegerField()
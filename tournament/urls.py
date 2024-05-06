from django.urls import *

from . import views
app_name = "tournament"

urlpatterns = [path("/teams",views.ListView.as_view()),name="teams",]
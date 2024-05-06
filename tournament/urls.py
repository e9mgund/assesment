from django.urls import path

from . import views
app_name = "tournament"

urlpatterns = [
    path("teams/",views.ListView.as_view(),name="teams"),
    path("teams/<int:country>",views.DetailView.as_view(),name="deatil")
    ]
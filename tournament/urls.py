from django.urls import path , include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'view',views.TeamViewSet)

app_name = "tournament"

urlpatterns = [
    path("teams/", views.ListView.as_view(), name="teams"),
    path("teams/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("teams/new/", views.fill, name="new"),
    path("api-auth/",include('rest_framework.urls')),
    path("",include(router.urls))
]
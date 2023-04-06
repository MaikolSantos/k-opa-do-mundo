from django.urls import path
from .views import TeamsView, TeamsDetailsView

urlpatterns = [
    path("teams/", TeamsView.as_view()),
    path("teams/<int:team_id>/", TeamsDetailsView.as_view()),
]

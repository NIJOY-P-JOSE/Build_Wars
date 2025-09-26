from django.urls import path
from . import views

urlpatterns = [
    # Main page: Shows the rank list
    # URL: /
    path('', views.leaderboard_view, name='leaderboard'),

    # Page to show the form for adding a new participant
    # URL: /add/
    path('add/', views.add_participant_view, name='add-participant'),

    # Page to edit an existing participant's details (like score)
    # The <int:participant_id> part is a variable that captures the participant's unique ID
    # URL examples: /edit/1/ or /edit/5/
    path('edit/<int:participant_id>/', views.edit_participant_view, name='edit-participant'),

    # API endpoint for the frontend to fetch live ranking data
    # URL: /api/ranking/
    path('api/ranking/', views.ranking_api, name='ranking-api'),
]


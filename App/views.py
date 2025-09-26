from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Participant
from .forms import ParticipantForm

def leaderboard_view(request):
    """
    Displays the main rank list page.
    It fetches all participants, and the model's 'Meta.ordering' handles the ranking.
    """
    participants = Participant.objects.all()
    context = {
        'participants': participants
    }
    return render(request, 'App/leaderboard.html', context)

def add_participant_view(request):
    """
    Handles the form for adding a new participant.
    """
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leaderboard')
    else:
        form = ParticipantForm()

    context = {
        'form': form,
        'form_title': 'Register New Participant'
    }
    return render(request, 'App/participant_form.html', context)

def edit_participant_view(request, participant_id):
    """
    Handles editing an existing participant, primarily for updating the score.
    """
    participant = get_object_or_404(Participant, id=participant_id)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('leaderboard')
    else:
        form = ParticipantForm(instance=participant)

    context = {
        'form': form,
        'form_title': f'Edit Score for {participant.name}'
    }
    return render(request, 'App/participant_form.html', context)

def ranking_api(request):
    """
    Provides the live ranking data as a JSON object for the frontend JavaScript.
    This will be used for the celebration visual.
    """
    participants = Participant.objects.all().values('id', 'name', 'score')
    data = list(participants)
    return JsonResponse(data, safe=False)

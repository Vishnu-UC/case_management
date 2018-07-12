# Create your views here.
from django.shortcuts import render

from .models import *


def display(request, courtcase_id):
    courtcase = CourtCase.objects.get(courtcase_id)
    party = Party.objects.filter(court_case=courtcase_id)
    context = {
        'courtcase': courtcase,
        'party': party
    }
    return render(request, 'polls/output.html', context)

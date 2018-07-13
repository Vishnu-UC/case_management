# Create your views here.
from django.shortcuts import render

from .models import *


def display(request, courtcase_id):
    courtcase = CourtCase.objects.get(id=courtcase_id)
    parties = Party.objects.filter(court_case=courtcase_id)
    context = {
        'courtcase': courtcase,
        'parties': parties
    }
    return render(request, 'courtdata/output.html', context)

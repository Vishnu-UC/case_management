# Create your views here.
from django.shortcuts import render

from .models import *


def display(request, courtcase_id):
    courtcase = CourtCase.objects.get(courtcase_id)
    party = Party.objects.filter(court_case=courtcase_id)
    case_type = MstCaseType.objects.get(pk=courtcase.mst_case_type)
    case_type_group = MstCaseTypeGroup.objects.get(pk=case_type.mst_case_type_group)
    case_type_category = MstCaseTypeCategory.objects.get(pk=case_type_group.mst_case_type_category)
    courthouse = MstCourthouse.objects.get(pk=courtcase.mst_courthouse)
    jurisdiction = MstJurisdiction.objects.get(pk=courthouse.mst_jurisdiction_id)
    context = {
        'courtcase': courtcase,
        'party': party,
        'case_type': case_type,
        'case_type_group': case_type_group,
        'case_type_category': case_type_category,
        'courthouse': courthouse,
        'jurisdiction': jurisdiction,
    }
    return render(request, 'polls/output.html', context)

from django.contrib import admin

from .models import *


@admin.register(MstPartyRepresentationType)
@admin.register(MstPartyType)
@admin.register(Attorney)
@admin.register(MstCaseTypeCategory)
@admin.register(MstCaseTypeGroup)
@admin.register(MstCaseType)
@admin.register(MstCaseStatusCategory)
@admin.register(MstCourthouse)
@admin.register(MstJurisdiction)
@admin.register(MstCaseStatus)
@admin.register(Party)
@admin.register(CourtCase)
class MstPartyRepresentationAdmin(admin.ModelAdmin):
    # list_display = ['name']
    search_fields = ['name']
    # readonly_fields = ['name']

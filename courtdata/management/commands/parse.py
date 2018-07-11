import argparse
import csv

from django.core.management.base import BaseCommand

from courtdata.models import *


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        file = options['filename']
        reader = csv.reader(file)
        for row in reader:
            obj1, created = MstCaseTypeCategory.get_or_create(name=row[4])
            obj2, created = MstCaseTypeGroup.get_or_create(mst_case_type_category=obj1.id, name=row[5])
            obj3, created = MstCaseType.get_or_create(mst_case_type_group=obj2.id, name=row[6])
            obj4, created = MstCaseStatusCategory.get_or_create(name=row[7])
            obj5, created = MstCaseStatus.get_or_create(name=row[8])
            obj6, created = MstJurisdiction.get_or_create(name=row[9])
            obj7, created = MstCourthouse.get_or_create(mst_jurisdiction=obj6.id, name=row[10])
            # case_key = models.CharField(max_length=25)
            # case_name = models.CharField(max_length=20)
            # case_number = models.CharField(max_length=20)
            # filing_date = models.DateField()
            # mst_case_type = models.ForeignKey(MstCaseType, on_delete=models.CASCADE)
            # mst_case_status = models.ForeignKey(MstCaseStatus, on_delete=models.CASCADE)
            # mst_case_status_category = models.ForeignKey(MstCaseStatusCategory, on_delete=models.CASCADE)
            # mst_courthouse = models.ForeignKey(MstCourthouse, on_delete=models.CASCADE)
            # judge_name = models.CharField(max_length=20)
            # created_date = models.DateTimeField()
            # last_update_date = models.DateTimeField()
            obj8 = CourtCase(case_key=row[0], case_name=row[1], case_number=row[2], filing_date=)

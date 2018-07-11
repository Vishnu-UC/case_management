import argparse
import csv
import re

from django.core.management.base import BaseCommand

from courtdata.models import *


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        file = options['filename']
        if re.search(r'UniCourt_Cases', options['filename']):
            reader = csv.reader(file)
            for row in reader:
                obj1, created = MstCaseTypeCategory.objects.get_or_create(name=row[4])
                obj2, created = MstCaseTypeGroup.objects.get_or_create(mst_case_type_category=obj1.id, name=row[5])
                obj3, created = MstCaseType.objects.get_or_create(mst_case_type_group=obj2.id, name=row[6])
                obj4, created = MstCaseStatusCategory.get_or_create(name=row[7])
                obj5, created = MstCaseStatus.objects.get_or_create(name=row[8])
                obj6, created = MstJurisdiction.objects.get_or_create(name=row[9])
                obj7, created = MstCourthouse.objects.get_or_create(mst_jurisdiction=obj6.id, name=row[10])
                obj8 = CourtCase(case_key=row[0], case_name=row[1], case_number=row[2], filing_date=row[3],
                                 mst_case_type=obj3.id, mst_case_status=obj5.id,
                                 mst_case_status_category=obj4.id, mst_courthouse=obj7.id, judge_name=row[13],
                                 created_date=row[11], last_update_date=row[12])
                obj1.save()
                obj2.save()
                obj3.save()
                obj4.save()
                obj5.save()
                obj6.save()
                obj7.save()
                obj8.save()
        elif CourtCase.objects.all.count() != 0:
            # court_case = models.ForeignKey(CourtCase, on_delete=models.CASCADE)
            # name = models.CharField(max_length=30)
            # mst_party_type = models.ForeignKey(MstPartyType, on_delete=models.CASCADE)
            # mst_party_representation_type = models.ForeignKey(MstPartyRepresentationType, on_delete=models.CASCADE)
            # attorney = models.ForeignKey(Attorney, on_delete=models.CASCADE)
            reader = csv.reader(file)
            for row in reader:
                obj1, created = MstPartyType.objects.get_or_create(name=row[2])
                obj2, created = MstPartyRepresentationType.objects.get_or_create(name=row[3])
                obj3, created = Attorney.objects.get_or_create(name=row[4])
                obj4 = CourtCase.objects.get(case_key=row[0])
                obj5 = Party(case_id=obj4.id, name=row[1], mst_party_type=obj1.id,
                             mst_party_representation_type=obj2.id, attorney=obj3.id)
                obj1.save()
                obj2.save()
                obj3.save()
                obj4.save()
                obj5.save()

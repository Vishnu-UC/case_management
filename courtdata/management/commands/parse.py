import argparse
import csv
import re

from django.core.management.base import BaseCommand

from courtdata.models import *


class CaseTypeCategory(object):

    def __init__(self):
        self.__name: str = None

    @property
    def name(self):
        return self.__name.strip().capitalize()

    @name.setter
    def name(self, name):
        if name is None:
            raise Exception("CAse category should set")
        self.__name = name


class CaseTypeGroup(object):

    def __init__(self):
        self.__name: str = None

    @property
    def name(self):
        return self.__name.strip().capitalize()

    @name.setter
    def name(self, name):
        if name is None:
            raise Exception("CAse type group should set")
        self.__name = name


class CaseType(object):

    def __init__(self):
        self.__name: str = None

    @property
    def name(self):
        return self.__name.strip().capitalize()

    @name.setter
    def name(self, name):
        if name is None:
            raise Exception("CAse type should set")
        self.__name = name


class CaseStatusCategory(object):

    def __init__(self):
        self.__name: str = None

    @property
    def name(self):
        return self.__name.strip().capitalize()

    @name.setter
    def name(self, name):
        if name is None:
            raise Exception("CAse status category should set")
        self.__name = name


class CaseStatus(object):

    def __init__(self):
        self.__name: str = None

    @property
    def name(self):
        return self.__name.strip().capitalize()

    @name.setter
    def name(self, name):
        if name is None:
            raise Exception("CAse status should set")
        self.__name = name


class Jurisdiction(object):

    def __init__(self):
        self.__name: str = None

    @property
    def name(self):
        return self.__name.strip().capitalize()

    @name.setter
    def name(self, name):
        if name is None:
            raise Exception("Case jurisdiction should set")
        self.__name = name


class Courthouse(object):

    def __init__(self):
        self.__name: str = None

    @property
    def name(self):
        return self.__name.strip().capitalize()

    @name.setter
    def name(self, name):
        if name is None:
            raise Exception("Case courthouse should set")
        self.__name = name


class PartyType(object):

    def __init__(self):
        self.__name: str = None

    @property
    def name(self):
        return self.__name.strip().capitalize()

    @name.setter
    def name(self, name):
        if name is None:
            raise Exception("CAse party type should set")
        self.__name = name


class PartyRepresentationType(object):
    # obj1, created = MstPartyType.objects.get_or_create(name=row[2])
    # obj2, created = MstPartyRepresentationType.objects.get_or_create(name=row[3])
    # obj3, created = Attorney.objects.get_or_create(name=row[4])
    # obj4 = CourtCase.objects.get(case_key=row[0])
    # obj5 = Party(case_id=obj4.id, name=row[1], mst_party_type=obj1.id,
    #              mst_party_representation_type=obj2.id, attorney=obj3.id)
    # obj5.save()
    def __init__(self):
        self.__name: str = None

    @property
    def name(self):
        return self.__name.strip().capitalize()

    @name.setter
    def name(self, name):
        if name is None:
            raise Exception("Case party represntation type should set")
        self.__name = name


class CAttorney(object):

    def __init__(self):
        self.__name: str = None

    @property
    def name(self):
        return self.__name.strip().capitalize()

    @name.setter
    def name(self, name):
        if name is None:
            raise Exception("Case attorney should set")
        self.__name = name


class CParty(object):

    def __init__(self):
        self.__name: str = None
        self.__party_type_object = None
        self.__party_representation_type_object = None
        self.__attorney_object = None
        self.__courtcase_object = None

    def set_party_type(self, party_type_name):
        party_type_object = CaseType()
        party_type_object.name = party_type_object
        dj_obj, _ = MstPartyType.objects.get_or_create(name=party_type__objectt.name)
        self.party_type_object = dj_obj

    def set_party_representation_type(self, party_type_name):
        set_party_representation_type = CaseType()
        set_party_representation_type_object.name = set_party_representation_type_object
        dj_obj, _ = MstPartyType.objects.get_or_create(name=party_type__objectt.name)
        self.party_type_object = dj_obj

    @property
    def name(self):
        return self.__name.strip().capitalize()

    @name.setter
    def name(self, name):
        if name is None:
            raise Exception("Case attorney should set")
        self.__name = name


class CCourtCase(object):
    def __init__(self):
        self.__case_key = None
        self.__case_name = None
        self.__case_number = None
        self.__filing_date = None
        self.__judge_name = None
        self.__created_date = None
        self.__last_update_date = None
        self.case_type_object = None
        self.case_type_group_object = None
        self.case_type_category_object = None
        self.case_status_category_object = None
        self.case_status_object = None
        self.jurisdiction_category_object = None
        self.courthouse_category_object = None

    def create(self, case_key, case_name, case_number, filing_date, judge_name, created_date, last_update_date):
        self.__case_key = case_key
        self.__case_name = case_name
        self.__case_number = case_number
        self.__filing_date = filing_date
        self.__judge_name = judge_name
        self.__created_date = created_date
        self.__last_update_date = last_update_date

    def save(self):
        obj8 = CourtCase(case_key=self.__case_key, case_name=self.__case_name, case_number=self.__case_number,
                         filing_date=self.__filing_date,
                         mst_case_type=self.case_type_object, mst_case_status=self.case_status_object,
                         mst_case_status_category=self.case_status_category_object,
                         mst_courthouse=self.courthouse_category_object, judge_name=self.__judge_name,
                         created_date=self.__created_date, last_update_date=self.__last_update_date)

        obj8.save()

    @property
    def case_key(self):
        return self.__case_key.strip().capitalize()

    @property
    def case_name(self):
        return self.__case_name.strip().capitalize()

    @property
    def case_number(self):
        return self.__case_number.strip().capitalize()

    @property
    def judge_name(self):
        return self.__judge_name.strip().capitalize()

    @case_key.setter
    def case_key(self, case_key):
        if case_key is None:
            raise Exception("Case attorney should set")
        self.__case_key = case_key

    @case_name.setter
    def case_name(self, case_name):
        if case_name is None:
            raise Exception("Case attorney should set")
        self.__case_name = case_name

    @case_number.setter
    def case_number(self, case_number):
        if case_number is None:
            raise Exception("Case attorney should set")
        self.__case_number = case_number

    @judge_name.setter
    def judge_name(self, judge_name):
        if judge_name is None:
            raise Exception("Case judge name should set")
        self.__judge_name = judge_name

    def set_case_type(self, case_type_name):
        case_type_object = CaseType()
        case_type_object.name = case_type_name
        dj_obj, _ = MstCaseType.objects.get_or_create(name=case_type_object.name)
        self.case_type_object = dj_obj

    def set_case_type_group(self, case_type_group_name):
        case_type_group_object = CaseTypeGroup()
        case_type_group_object.name = case_type_group_name
        dj_obj, _ = MstCaseTypeGroup.objects.get_or_create(name=case_type_group_object.name)
        self.case_type_group_object = dj_obj

    def set_case_type_category(self, case_type_category_name):
        case_type_category_object = CaseTypeCategory()
        case_type_category_object.name = case_type_category_name
        dj_obj, _ = MstCaseTypeCategory.objects.get_or_create(name=case_type_category_object.name)
        self.case_type_category_object = dj_obj

    def set_case_status_category(self, case_status_category_name):
        case_status_category_object = CaseStatusCategory()
        case_status_category_object.name = case_status_category_name
        dj_obj, _ = MstCaseStatusCategory.objects.get_or_create(name=case_status_category_object.name)
        self.case_status_category_object = dj_obj

    def set_case_status(self, case_status_name):
        case_status_object = CaseStatus()
        case_status_object.name = case_status_name
        dj_obj, _ = MstCaseStatus.objects.get_or_create(name=case_status_object.name)
        self.case_status_object = dj_obj

    def set_jurisdiction(self, jurisdiction_name):
        jurisdiction_object = Jurisdiction()
        jurisdiction_object.name = jurisdiction_name
        dj_obj, _ = MstJurisdiction.objects.get_or_create(name=jurisdiction_object.name)
        self.jurisdiction_category_object = dj_obj

    def set_courthouse(self, courthouse_name):
        courthouse_object = Courthouse()
        courthouse_object.name = courthouse_name
        dj_obj, _ = MstCourthouse.objects.get_or_create(name=courthouse_object.name)
        self.courthouse_category_object = dj_obj


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        x = CaseTypeCategory()
        x.name = "ABC"

        file = options['filename']
        if re.search(r'UniCourt_Cases', options['filename']):
            reader = csv.reader(file)
            for row in reader:
                c = CCourtCase()
                c.create('x', 'y')
                c.set_case_type('ct')
                c.save()

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

                obj8.save()
        elif CourtCase.objects.all.count() != 0:
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

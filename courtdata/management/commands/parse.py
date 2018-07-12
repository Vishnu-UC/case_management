import argparse
import csv
import re
from datetime import datetime

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
        self.__court_case_id = None
        self.__party_type_object = None
        self.__party_representation_type_object = None
        self.__attorney_object = None
        self.__courtcase_object = None

    def create(self, name):
        self.__name = name

    def save(self):
        obj = Party(court_case=self.__courtcase_object, name=self.__name, mst_party_type=self.__party_type_object,
                    mst_party_representation_type=self.__party_representation_type_object,
                    attorney=self.__attorney_object)
        obj.save()

    def set_party_type(self, party_type_name):
        party_type_object = CaseType()
        party_type_object.name = party_type_name
        dj_obj, _ = MstPartyType.objects.get_or_create(name=party_type_object.name)
        self.__party_type_object = dj_obj

    def set_party_representation_type(self, party_representation_type_name):
        party_representation_type_object = CaseType()
        party_representation_type_object.name = party_representation_type_name
        dj_obj, _ = MstPartyRepresentationType.objects.get_or_create(name=party_representation_type_object.name)
        self.__party_representation_type_object = dj_obj

    def find_courtcase(self, case_id):
        courtcase_object = CourtCase.objects.get(case_key=case_id)
        self.__courtcase_object = courtcase_object

    def set_attorney(self, attorney_name):
        attorney_object = CAttorney()
        attorney_object.name = attorney_name
        dj_obj, _ = Attorney.objects.get_or_create(name=attorney_object.name)
        self.__attorney_object = dj_obj

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
        self.__case_type_object = None
        self.__case_type_group_object = None
        self.__case_type_category_object = None
        self.__case_status_category_object = None
        self.__case_status_object = None
        self.__jurisdiction_object = None
        self.__courthouse_object = None

    def create(self, case_key, case_name, case_number, filing_date, judge_name, created_date, last_update_date):
        self.__case_key = case_key
        self.__case_name = case_name
        self.__case_number = case_number
        self.__filing_date = datetime.strptime(filing_date, '%m/%d/%Y')
        self.__judge_name = judge_name
        self.__created_date = datetime.strptime(created_date, '%m/%d/%Y %H:%M:%S')
        self.__last_update_date = datetime.strptime(last_update_date, '%m/%d/%Y %H:%M:%S')

    def save(self):
        obj, _ = CourtCase.objects.get_or_create(case_key=self.__case_key, case_name=self.__case_name,
                                                 case_number=self.__case_number, filing_date=self.__filing_date,
                                                 mst_case_type=self.__case_type_object,
                                                 mst_case_status=self.__case_status_object,
                                                 mst_case_status_category=self.__case_status_category_object,
                                                 mst_courthouse=self.__courthouse_object,
                                                 judge_name=self.__judge_name,
                                                 created_date=self.__created_date,
                                                 last_update_date=self.__last_update_date)

        obj.save()

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
        dj_obj, _ = MstCaseType.objects.get_or_create(mst_case_type_group=self.__case_type_group_object,
                                                      name=case_type_object.name)
        self.__case_type_object = dj_obj

    def set_case_type_group(self, case_type_group_name):
        case_type_group_object = CaseTypeGroup()
        case_type_group_object.name = case_type_group_name
        dj_obj, _ = MstCaseTypeGroup.objects.get_or_create(mst_case_type_category=self.__case_type_category_object,
                                                           name=case_type_group_object.name)
        self.__case_type_group_object = dj_obj

    def set_case_type_category(self, case_type_category_name):
        case_type_category_object = CaseTypeCategory()
        case_type_category_object.name = case_type_category_name
        dj_obj, _ = MstCaseTypeCategory.objects.get_or_create(name=case_type_category_object.name)
        self.__case_type_category_object = dj_obj

    def set_case_status_category(self, case_status_category_name):
        case_status_category_object = CaseStatusCategory()
        case_status_category_object.name = case_status_category_name
        dj_obj, _ = MstCaseStatusCategory.objects.get_or_create(name=case_status_category_object.name)
        self.__case_status_category_object = dj_obj

    def set_case_status(self, case_status_name):
        case_status_object = CaseStatus()
        case_status_object.name = case_status_name
        dj_obj, _ = MstCaseStatus.objects.get_or_create(name=case_status_object.name)
        self.__case_status_object = dj_obj

    def set_jurisdiction(self, jurisdiction_name):
        jurisdiction_object = Jurisdiction()
        jurisdiction_object.name = jurisdiction_name
        dj_obj, _ = MstJurisdiction.objects.get_or_create(name=jurisdiction_object.name)
        self.__jurisdiction_object = dj_obj

    def set_courthouse(self, courthouse_name):
        courthouse_object = Courthouse()
        courthouse_object.name = courthouse_name
        dj_obj, _ = MstCourthouse.objects.get_or_create(mst_jurisdiction=self.__jurisdiction_object,
                                                        name=courthouse_object.name)
        self.__courthouse_object = dj_obj


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        file = options['filename']
        if re.search(r'UniCourt_Cases', str(options['filename'])):
            reader = csv.reader(file)
            for row in list(reader)[1:]:
                c = CCourtCase()
                c.create(row[0], row[1], row[2], row[3], row[13], row[11], row[12])
                c.set_case_type_category(row[4])
                c.set_case_type_group(row[5])
                c.set_case_type(row[6])
                c.set_case_status_category(row[7])
                c.set_case_status(row[8])
                c.set_jurisdiction(row[9])
                c.set_courthouse(row[10])
                c.save()

        elif len(CourtCase.objects.all()) != 0:
            reader = csv.reader(file)
            for row in list(reader)[1:]:
                p = CParty()
                p.create(row[1])
                p.set_party_type(row[2])
                p.set_party_representation_type(row[3])
                p.set_attorney(row[4])
                p.find_courtcase(row[0])
                p.save()

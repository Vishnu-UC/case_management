from django.core.management.base import BaseCommand

from courtdata.models import CourtCase


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        print(CourtCase.objects.all().query)

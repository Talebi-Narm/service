from django.core.management.base import BaseCommand
from faker import Faker

from django.db import transaction

class Command(BaseCommand):
    help = "generate fake data"

    @transaction.atomic
    def handle(self, *args, **options):
        faker = Faker()

from django.core.management.base import BaseCommand
from faker import Faker
from common.models import Tag

from django.db import transaction

class Command(BaseCommand):
    help = "generate fake data"

    @transaction.atomic
    def handle(self, *args, **options):
        faker = Faker()

        # new tags
        tag_list = [
            "Apartment",
            "Home",
            "Drug",
            "Tropical",
            "Cold",
            "Tree"
        ]

        Tag.objects.all().delete()
        for tag in tag_list:
            temp = Tag(
                name = tag,
                description = faker.text()
            )
            temp.save()

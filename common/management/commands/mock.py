from django.core.management.base import BaseCommand
from faker import Faker
from store.models import *
from common.models import Tag
import random

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

        tags = list(Tag.objects.all())

        # new plants
        plant_list = [
            "Marijuana",
            "Opium",
            "Weed",
            "Bluestem",
            "Caladium",
            "Canna Lily",
            "Blue Fescue",
            "Creeping Zinnia",
            "Fan Flower"
        ]
        Plant.objects.all().delete()
        for plant in plant_list:
            temp = Plant(
                name = plant,
                description = faker.text(),
                count = faker.random_int(0, 100),
                price = faker.random_int(10, 10000) / 100,
                main_image = faker.image_url(),
                environment = faker.random_int(0, 2),
                water = faker.random_int(0, 2),
                light = faker.random_int(0, 2),
                growth_rate = faker.random_int(0, 2)
            )
            count = faker.random_int(0, len(tag_list))
            temp.tags.add(random.choices(tags, k=count))
            temp.save()

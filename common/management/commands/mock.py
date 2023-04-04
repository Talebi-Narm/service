from django.core.management.base import BaseCommand
from faker import Faker
from store.models import *
from common.models import Tag
from user.models import User
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

        # new tools
        tool_list = [
            "Apron",
            "Axe",
            "Boots",
            "Bucket",
            "Fence",
            "Fertilizer",
            "Flowerpot",
            "Garden hose",
            "Garden trowel",
            "Gardening fork",
            "Gardening gloves",
            "Hedge shears",
            "Hoe",
            "Pruning saw",
            "Rake"
        ]
        Tool.objects.all().delete()
        for tool in tool_list:
            temp = Tool(
                name = tool,
                description = faker.text(),
                count = faker.random_int(0, 100),
                price = faker.random_int(10, 10000) / 100,
                main_image = faker.image_url()
            )
            count = faker.random_int(0, len(tag_list))
            temp.tags.add(random.choices(tags, k=count))
            temp.save()

        # new users
        User.objects.all().delete()
        temp = User(
            username = "Admin",
            first_name = "Admin",
            last_name = "Admini",
            email = "admin@talebi-narm.ir",
            password = "AdminTalebi",
            is_active = True,
            is_staff = True,
            is_superuser = True
        )
        temp.save()
        
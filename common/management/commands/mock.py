import random

from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from common.models import Tag
from store.models import *
from user.models import User


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
        for tag_name in tag_list:
            temp = Tag(
                name=tag_name,
                description=faker.text()
            )
            temp.save()

        tags_id = list(map(lambda x: x[0], list(Tag.objects.values_list('id'))))

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
        for plant_name in plant_list:
            temp = Plant(
                name=plant_name,
                description=faker.text(),
                count=faker.random_int(0, 100),
                price=faker.random_int(10, 10000) / 100,
                main_image=faker.image_url(),
                environment=faker.random_int(0, 2),
                water=faker.random_int(0, 2),
                light=faker.random_int(0, 2),
                growth_rate=faker.random_int(0, 2)
            )
            count = faker.random_int(0, len(tag_list))
            random_tags_id = random.choices(tags_id, k=count)
            for random_tag_id in random_tags_id:
                temp.tags.add(random_tag_id)
            temp.save()
        print("plants created.")

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
                name=tool,
                description=faker.text(),
                count=faker.random_int(0, 100),
                price=faker.random_int(10, 10000) / 100,
                main_image=faker.image_url()
            )
            count = faker.random_int(0, len(tag_list))
            random_tags_id = random.choices(tags_id, k=count)
            for random_tag_id in random_tags_id:
                temp.tags.add(random_tag_id)
            temp.save()

        # new users
        User.objects.all().delete()
        temp = User(
            username="Talebi",
            first_name="Talebi",
            last_name="Admini",
            email="Talebi@talebi-narm.ir",
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        temp.set_password("TalebiAdmin1234")
        temp.save()
        print("one admin created.")

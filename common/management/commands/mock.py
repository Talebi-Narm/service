import random

from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from common.models import Tag
from store.models import Plant, Tool
from user.models import User


class Command(BaseCommand):
    help = "generate fake data!"

    @transaction.atomic
    def handle(self, *args, **options):
        faker = Faker()

        Plant.objects.all().delete()
        Tool.objects.all().delete()
        Tag.objects.all().delete()
        User.objects.all().delete()

        tags_id = list(map(lambda x: x[0], list(Tag.objects.values_list('id'))))

        create_tags(faker)
        create_plants(faker, tags_id)
        create_tools(faker, tags_id)
        create_users()


def create_album(faker: Faker, count: int) -> dict:
    temp = dict()
    for index in range(random.randint(0, count)):
        name = f"pic{index + 1}"
        temp[name] = faker.image_url()
    return temp


def create_tags(faker: Faker):
    tag_list = [
        "Discount",
        "Apartment",
        "Home",
        "Drug",
        "Tropical",
        "Cold",
        "Tree"
    ]

    for tag_name in tag_list:
        temp = Tag(
            name=tag_name,
            description=faker.text()
        )
        temp.save()
    print("Tags created.")


def create_plants(faker: Faker, tags_id: list):
    plants_list = [
        "Marijuana",
        "Opium",
        "Weed",
        "Blossom",
        "Caladium",
        "Canna Lily",
        "Hazel",
        "Sanvitalia",
        "Scaevola",
        "Juniper",
        "Azalea",
        "Dahlia",
        "Hedera"
    ]
    plant_images_list = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Hampa_Cannabis_sativa_L._%28n%C3%A4rbild%29.jpg/330px-Hampa_Cannabis_sativa_L._%28n%C3%A4rbild%29.jpg", # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Opium_pod_cut_to_demonstrate_fluid_extraction1.jpg/330px-Opium_pod_cut_to_demonstrate_fluid_extraction1.jpg", # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Stairs_with_weed.jpg/330px-Stairs_with_weed.jpg", # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Badamwari_Flower_Series_2.png/330px-Badamwari_Flower_Series_2.png", # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Caladium_schomburgkii_changjur-1-yercaud-salem-India.JPG/330px-Caladium_schomburgkii_changjur-1-yercaud-salem-India.JPG", # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Canna_sp.jpg/330px-Canna_sp.jpg",  # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Corylus_avellana_0001.JPG/330px-Corylus_avellana_0001.JPG", # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Sanvitalia_procumbens_-_plants_%28aka%29.jpg/330px-Sanvitalia_procumbens_-_plants_%28aka%29.jpg", # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Starr_020925-0070_Scaevola_chamissoniana.jpg/330px-Starr_020925-0070_Scaevola_chamissoniana.jpg", # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Juniperus_osteosperma_1.jpg/330px-Juniperus_osteosperma_1.jpg", # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Azalea.750pix.jpg/330px-Azalea.750pix.jpg",  # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Dahlia_x_hybrida.jpg/330px-Dahlia_x_hybrida.jpg", # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Hedera_algeriensis_kz01.jpg/330px-Hedera_algeriensis_kz01.jpg" # noqa
    ]

    for plant in range(len(plants_list)):
        temp = Plant(
            name=plants_list[plant],
            description=faker.text(),
            count=faker.random_int(0, 100),
            price=faker.random_int(10, 10000) / 100,
            main_image=plant_images_list[plant],
            environment=faker.random_int(0, 2),
            water=faker.random_int(0, 2),
            light=faker.random_int(0, 2),
            growth_rate=faker.random_int(0, 2)
        )
        count = faker.random_int(0, len(tags_id))
        random_tags_id = random.choices(tags_id, k=count)
        for random_tag_id in random_tags_id:
            temp.tags.add(random_tag_id)
        temp.album = create_album(faker, 5)
        temp.save()
    print("Plants created.")


def create_tools(faker: Faker, tags_id: list):
    tools_list = [
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
        "Chainsaw",
        "saw",
        "Rake"
    ]
    tool_images_list = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Felling_axe.jpg/330px-Felling_axe.jpg",  # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Cowboy_boots.jpg/300px-Cowboy_boots.jpg",  # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Gotland-Bottarve_Museumshof_07.jpg/375px-Gotland-Bottarve_Museumshof_07.jpg", # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Westtown.jpg/330px-Westtown.jpg",  # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Manure_spreading_Hlokozi_2007_11_29.jpg/495px-Manure_spreading_Hlokozi_2007_11_29.jpg", # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Shelves_of_flower_pots_in_Darwin%27s_laboratory%2C_Down_House_-_geograph.org.uk_-_1200541.jpg/330px-Shelves_of_flower_pots_in_Darwin%27s_laboratory%2C_Down_House_-_geograph.org.uk_-_1200541.jpg", # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Garden_hose.jpg/330px-Garden_hose.jpg",  # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Masons_trowel.jpg/390px-Masons_trowel.jpg",  # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Bar_spade.jpg/255px-Bar_spade.jpg",  # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Centre_de_Documentaci%C3%B3_Museu_T%C3%A8xtil_de_Terrassa-_Reserves-_Teixits-_Guants002.JPG/330px-Centre_de_Documentaci%C3%B3_Museu_T%C3%A8xtil_de_Terrassa-_Reserves-_Teixits-_Guants002.JPG", # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Hedge_Trimming_-_Kolkata_2005-08-10_02050.JPG/330px-Hedge_Trimming_-_Kolkata_2005-08-10_02050.JPG", # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Chainsaw.JPG/330px-Chainsaw.JPG",  # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Crosscut_saw.JPG/375px-Crosscut_saw.JPG",  # noqa
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Wooden_rake.jpg/330px-Wooden_rake.jpg"  # noqa
    ]

    for tool in range(len(tools_list)):
        temp = Tool(
            name=tools_list[tool],
            description=faker.text(),
            count=faker.random_int(0, 100),
            price=faker.random_int(10, 10000) / 100,
            main_image=tool_images_list[tool]
        )
        count = faker.random_int(0, len(tags_id))
        random_tags_id = random.choices(tags_id, k=count)
        for random_tag_id in random_tags_id:
            temp.tags.add(random_tag_id)
        temp.album = create_album(faker, 5)
        temp.save()
    print("Tools created.")


def create_users():
    # default
    temp = User(
        username="Talebi",
        first_name="Talebi",
        last_name="Admini",
        email="admin@talebi-narm.ir",
        gender=3,
        is_active=True,
        is_staff=True,
        is_superuser=True
    )
    temp.set_password("TalebiAdmin1234")
    temp.save()

    # Amir Mohammad
    amir_mohammad = User(
        username="Amir-Mohammad",
        first_name="Amir Mohammad",
        last_name="Sohrabi",
        email="the.am.sohrabi@gmail.com",
        gender=0,
        is_active=True,
        is_staff=True,
        is_superuser=True
    )
    amir_mohammad.set_password("painisreal")
    amir_mohammad.save()

    # Narges
    narges = User(
        username="Narges",
        first_name="Narges",
        last_name="Mashayekhi",
        email="nmashayekhi30@yahoo.com",
        gender=1,
        is_active=True,
        is_staff=True,
        is_superuser=True
    )
    narges.set_password("painisreal")
    narges.save()

    # Deniz
    deniz = User(
        username="Deniz",
        first_name="Deniz",
        last_name="Ahmadi",
        email="ahmadideniz@gmail.com",
        gender=1,
        is_active=True,
        is_staff=True,
        is_superuser=True
    )
    deniz.set_password("painisreal")
    deniz.save()

    # Hamed
    hamed = User(
        username="Hamed",
        first_name="Hamed",
        last_name="Feiz Abadi",
        email="hamed@talebi-narm.ir",
        gender=0,
        is_active=True,
        is_staff=True,
        is_superuser=True
    )
    hamed.set_password("123456")
    hamed.save()

    # Navid
    navid = User(
        username="Navid",
        first_name="Navid",
        last_name="Mousavizade",
        email="navid@talebi-narm.ir",
        gender=0,
        is_active=True,
        is_staff=True,
        is_superuser=True
    )
    navid.set_password("painisreal")
    navid.save()

    print("Admins created.")

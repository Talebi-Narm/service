import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from store.models import Plant
from store.serializers.product import PlantAdminSerializer

client = Client()


class PlantAdminTest(TestCase):
    """Test module for testing all plant admin apis"""

    def setUp(self):
        self.test1 = {
            'name': 'test 1',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'count': 5,
            'price': 100,
            'main_image': 'image1',
            'environment': 0,
            'water': 1,
            'light': 0,
            'growth_rate': 2
        }
        self.test2 = {
            'name': 'test 2',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'count': 23,
            'price': 1200,
            'main_image': 'image2',
            'environment': 1,
            'water': 2,
            'light': 1,
            'growth_rate': 1
        }
        self.test3 = {
            'name': 'test 3',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'count': 41,
            'price': 235,
            'main_image': 'image3',
            'environment': 2,
            'water': 1,
            'light': 2,
            'growth_rate': 0
        }
        self.test4_invalid = {
            'name': 'test 4',
            'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'count': 55,
            'price': 23,
            'main_image': 'image4',
            'environment': 3,
            'water': 1,
            'light': 0,
            'growth_rate': 2
        }

        def test_create_valid_plant(self):
            response = client.post(
                reverse('admin_plants'),
                data=json.dumps(self.test1),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            response = client.post(
                reverse('admin_plants'),
                data=json.dumps(self.test2),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            response = client.post(
                reverse('admin_plants'),
                data=json.dumps(self.test3),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        def test_create_invalid_plant(self):
            response = client.post(
                reverse('admin_plants'),
                data=json.dumps(self.test4_invalid),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        def test_get_all_plants(self):
            response = client.get(reverse('admin_plants'))
            plants = Plant.objects.all()
            serializer = PlantAdminSerializer(plants, many=True)
            self.assertEqual(response.data, serializer.data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_get_valid_single_plant(self):
            response = client.get(
                reverse('admin_plants_detail', kwargs={'pk': Plant.objects.all().first()}))
            plant = Plant.objects.all().first()
            serializer = PlantAdminSerializer(plant)
            self.assertEqual(response.data, serializer.data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_get_invalid_single_plant(self):
            response = client.get(
                reverse('admin_plants_detail', kwargs={'pk': 1}))
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        def test_valid_update_plant(self):
            response = client.put(
                reverse('admin_plants_detail', kwargs={'pk': Plant.objects.all().first()}),
                data=json.dumps(self.test1),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        def test_invalid_update_plant(self):
            response = client.put(
                reverse('admin_plants_detail', kwargs={'pk': Plant.objects.all().first()}),
                data=json.dumps(self.test4_invalid),
                content_type='application/json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        def test_valid_delete_plant(self):
            response = client.delete(
                reverse('admin_plants_detail', kwargs={'pk': Plant.objects.all().first()}))
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

            response = client.delete(
                reverse('admin_plants_detail', kwargs={'pk': Plant.objects.all().first()}))
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

            response = client.delete(
                reverse('admin_plants_detail', kwargs={'pk': Plant.objects.all().first()}))
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        def test_invalid_delete_plant(self):
            response = client.delete(
                reverse('admin_plants_detail', kwargs={'pk': 1}))
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

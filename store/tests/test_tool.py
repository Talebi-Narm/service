from django.test import TestCase, Client
import json
from rest_framework import status
from django.urls import reverse
from store.serializers.product import *
from store.models import Tool, Tool

client = Client()

class ToolAdminTest(TestCase):
    """Test module for testing all tool admin apis"""

    def setUp(self):
        self.test1 = {
            'name':'test 1',
            'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'count':5,
            'price':100,
            'main_image':'image1'
        }
        self.test2 = {
            'name':'test 2',
            'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'count':23,
            'price':1200,
            'main_image':'image2'
        }
        self.test3 = {
            'name':'test 3',
            'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'count':41,
            'price':235,
            'main_image':'image3'
        }
        self.test4_invalid = {
            'name':'test 4',
            'description':'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
            'count':55,
            'price':'23',
            'main_image':'image4'
        }

        def test_create_valid_tool(self):
            response = client.post(
                reverse('tools'),
                data=json.dumps(self.test1),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            response = client.post(
                reverse('tools'),
                data=json.dumps(self.test2),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            response = client.post(
                reverse('tools'),
                data=json.dumps(self.test3),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        def test_create_invalid_tool(self):
            response = client.post(
                reverse('tools'),
                data=json.dumps(self.test4_invalid),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        def test_get_all_tools(self):
            response = client.get(reverse('tools'))
            tools = Tool.objects.all()
            serializer = ToolSerializer(tools, many=True)
            self.assertEqual(response.data, serializer.data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_get_valid_single_tool(self):
            response = client.get(
                reverse('tools_detail', kwargs={'pk': Tool.objects.all().first()}))
            tool = Tool.objects.all().first()
            serializer = ToolSerializer(tool)
            self.assertEqual(response.data, serializer.data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_get_invalid_single_tool(self):
            response = client.get(
                reverse('tools_detail', kwargs={'pk': 1}))
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        def test_valid_update_tool(self):
            response = client.put(
                reverse('tools_detail', kwargs={'pk': Tool.objects.all().first()}),
                data=json.dumps(self.test1),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        def test_invalid_update_tool(self):
            response = client.put(
                reverse('tools_detail', kwargs={'pk': Tool.objects.all().first()}),
                data=json.dumps(self.test4_invalid),
                content_type='application/json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        def test_valid_delete_tool(self):
            response = client.delete(
                reverse('tools_detail', kwargs={'pk': Tool.objects.all().first()}))
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

            response = client.delete(
                reverse('tools_detail', kwargs={'pk': Tool.objects.all().first()}))
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

            response = client.delete(
                reverse('tools_detail', kwargs={'pk': Tool.objects.all().first()}))
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        def test_invalid_delete_tool(self):
            response = client.delete(
                reverse('tools_detail', kwargs={'pk': 1}))
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
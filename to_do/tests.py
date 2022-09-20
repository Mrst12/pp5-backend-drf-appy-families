'''Automated testing for the Todo app'''
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Todo


class TodoListViewTests(APITestCase):
    '''tests for the list view'''
    def setUp(self):
        '''run before each test'''
        User.objects.create_user(username='lisa', password='pass')

    def test_can_list_tasks(self):
        '''make sure tasks can be listed'''
        lisa = User.objects.get(username='lisa')
        Todo.objects.create(owner=lisa, task_title='lisas title', due_date='2022-09-22')
        response = self.client.get('/to_do/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

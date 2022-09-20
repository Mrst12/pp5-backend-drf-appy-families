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
        Todo.objects.create(owner=lisa, task_title='lisas title')
        response = self.client.get('/to_do/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_task(self):
        '''check a task can be created if logged in'''
        self.client.login(username='lisa', password='pass')
        response = self.client.post('/to_do/', {'task_title': 'lisas title'})
        count = Todo.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cannot_create_task(self):
        '''test task cannot be created if user not logged in'''
        response = self.client.post('/to_do/', {'task_title': 'lisas title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

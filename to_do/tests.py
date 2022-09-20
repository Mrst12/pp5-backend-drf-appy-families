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


class TodoDetailViewTests(APITestCase):
    '''testing the detail view of the Todo app'''
    def setUp(self):
        '''run before each test'''
        lisa = User.objects.create_user(username='lisa', password='pass')
        michael = User.objects.create_user(username='michael', password='pass')
        Todo.objects.create(
            owner=lisa, task_title='lisas title'
        )
        Todo.objects.create(
            owner=michael, task_title='michaels title'
        )

    def test_can_retrieve_task_with_valid_id(self):
        '''test task can be retrieved with valid id'''
        response = self.client.get('/to_do/1/')
        self.assertEqual(response.data['task_title'], 'lisas title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_task_with_invalid_id(self):
        '''test an invalid id cannot bring up the task'''
        response = self.client.get('/to_do/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_task(self):
        '''test the owner of task can update it'''
        self.client.login(username='lisa', password='pass')
        response = self.client.put('/to_do/1/', {'task_title': 'a new title'})
        todo = Todo.objects.filter(pk=1).first()
        self.assertEqual(todo.task_title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_task_they_dont_own(self):
        '''test for making sure a task not owned by user cannot be updated'''
        self.client.login(username='lisa', password='pass')
        response = self.client.put('/to_do/2/', {'task_title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

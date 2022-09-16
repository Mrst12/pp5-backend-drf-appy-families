'''tests for the achievement app'''
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Achievements


class AchievementListViewTests(APITestCase):
    '''testing list view for achievements'''
    def setUp(self):
        '''run before each test'''
        User.objects.create_user(username='lisa', password='pass')

    def test_can_list_achievements(self):
        '''test user can retrieve all achievements'''
        lisa = User.objects.get(username='lisa')
        Achievements.objects.create(owner=lisa, title='any title')
        response = self.client.get('/achievements/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_achievement(self):
        '''logged in user can create'''
        self.client.login(username='lisa', password='pass')
        response = self.client.post('/achievements/', {'title': 'my title'})
        count = Achievements.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_cant_create_achievement(self):
        '''test for logged out user unable to create achievement'''
        response = self.client.post('/achievements/', {'title': 'my title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

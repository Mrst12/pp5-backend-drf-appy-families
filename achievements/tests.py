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


class AchievementDetailViewTests(APITestCase):
    '''testing detail view for achievements'''
    def setUp(self):
        '''run before each test'''
        lisa = User.objects.create_user(username='lisa', password='pass')
        michael = User.objects.create_user(username='michael', password='pass')
        Achievements.objects.create(
            owner=lisa, title='my title', content='lisascontent'
        )
        Achievements.objects.create(
            owner=michael, title='his title', content='michaels content'
        )

    def test_can_retrieve_achievement_using_valid_id(self):
        '''test valid id shows post'''
        response = self.client.get('/achievements/1/')
        self.assertEqual(response.data['title'], 'my title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        '''test invalid id does not show post'''
        response = self.client.get('/achievements/99/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_achievement(self):
        '''can owner update'''
        self.client.login(username='lisa', password='pass')
        response = self.client.put(
            '/achievements/1/', {'title': 'a new title'}
        )
        post = Achievements.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_unowned_post(self):
        '''check user cant update someone elses post'''
        self.client.login(username='lisa', password='pass')
        response = self.client.put(
            '/achievements/2/', {'title': 'a new title'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

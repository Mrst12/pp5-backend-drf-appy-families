'''Testing for the memo posts, list and detail'''
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Memo


# taken from DRF_API walkthrough with modifications
class MemoListViewTests(APITestCase):
    '''test the memo list view'''
    def setUp(self):
        '''setup runs before every test method'''
        User.objects.create_user(username='lisa', password='pass')

    def test_can_list_memos(self):
        '''check a user can list all the posts'''
        lisa = User.objects.get(username='lisa')
        Memo.objects.create(owner=lisa, content='testing memos')
        response = self.client.get('/memo_posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_memo(self):
        '''test to see if logged in user can create a post'''
        self.client.login(username='lisa', password='pass')
        response = self.client.post('/memo_posts/', {'content': 'testing'})
        count = Memo.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cannot_create_memo(self):
        '''test for non logged in user unable to post memos'''
        response = self.client.post('/memo_posts/', {'content': 'testing again'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

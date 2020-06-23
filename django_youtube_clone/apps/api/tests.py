from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from django_youtube_clone.apps.account.models import Profile


class LoginApiTests(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='testUser', email='test@test.com', password='rightPW')
        self.token = Token.objects.create(user=self.test_user)
        self.url = reverse('login_api')

    def test_login_with_wrong_user(self):
        wrong_user = {
            'username': 'wrongUser',
            'password': 'wrongPW'
        }
        resp = self.client.post(self.url, wrong_user)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_with_right_user(self):
        right_user = {
            'username': 'testUser',
            'password': 'rightPW'
        }
        resp = self.client.post(self.url, right_user)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, {'token': self.token.key, 'username': self.test_user.username})

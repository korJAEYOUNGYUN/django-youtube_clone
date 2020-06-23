from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch

from .models import Profile


def setup_default_user():
    test_user = User.objects.create_user(username='testUser', email='test@test.com', password='0000')
    Profile.objects.create(user=test_user)
    return test_user


class ProfileModelTests(TestCase):
    def setUp(self):
        self.test_user = setup_default_user()

    def test_default_profile(self):
        default_profile = self.test_user.profile
        self.assertEqual(str(default_profile), self.test_user.username)
        self.assertEqual(default_profile.avatar.name, 'uploads/avatars/no_avatar.png')


class EditProfileViewTests(TestCase):
    def setUp(self):
        self.url = reverse('edit_profile')
        self.c = Client()
        self.test_user = setup_default_user()

    def test_get_edit_profile_without_login(self):
        self.c.logout()
        res = self.c.get(self.url)
        self.assertEqual(res.status_code, 302)

    def test_get_edit_profile_with_login(self):
        self.assertTrue(self.c.login(username=self.test_user.username, password='0000'))
        res = self.c.get(self.url)
        self.assertEqual(res.status_code, 200)

    def test_post_edit_profile(self):
        self.assertTrue(self.c.login(username=self.test_user.username, password='0000'))
        self.c.post(self.url, {'username': 'testUser2', 'email': 'test2@test.com'})
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username='testUser')
        test_user = User.objects.get(username='testUser2')
        self.assertTrue(test_user.email, 'test2@test.com')


class ChangePasswordViewTests(TestCase):
    def setUp(self):
        self.url = reverse('change_password')
        self.c = Client()
        self.test_user = setup_default_user()

    def test_get_change_password_without_login(self):
        res = self.c.get(self.url)
        self.assertEqual(res.status_code, 302)

    def test_get_change_password_with_login(self):
        self.assertTrue(self.c.login(username=self.test_user.username, password='0000'))
        res = self.c.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.c.logout()

    def test_post_change_password_with_wrong_original_password(self):
        self.assertTrue(self.c.login(username=self.test_user.username, password='0000'))
        self.c.post(self.url, {'original_password': '0001', 'new_password': '0002', 'new_password2': '0002'})
        self.c.logout()
        self.assertFalse(self.c.login(username=self.test_user.username, password='0002'))
        self.c.logout()

    def test_post_change_password_with_wrong_new_password(self):
        self.assertTrue(self.c.login(username=self.test_user.username, password='0000'))
        self.c.post(self.url, {'original_password': '0000', 'new_password': '0002', 'new_password2': '0003'})
        self.c.logout()
        self.assertFalse(self.c.login(username=self.test_user.username, password='0002'))
        self.c.logout()

    def test_post_change_password_with_right_new_password(self):
        self.assertTrue(self.c.login(username=self.test_user.username, password='0000'))
        self.c.post(self.url, {'original_password': '0000', 'new_password': '0002', 'new_password2': '0002'})
        self.c.logout()
        self.assertTrue(self.c.login(username=self.test_user.username, password='0002'))
        self.c.logout()


class JoinViewTests(TestCase):
    def setUp(self):
        self.url = reverse('join')
        self.c = Client()

    def test_post_join_with_different_password(self):
        self.c.post(self.url, {'username': 'testUser', 'email': 'test@test.com', 'password': '0000', 'password2': '0001'})
        self.assertFalse(self.c.login(username='testUser', password='0000'))
        self.assertFalse(self.c.login(username='testUser', password='0001'))

    def test_post_join_with_right_password(self):
        self.c.post(self.url, {'username': 'testUser', 'email': 'test@test.com', 'password': '0000', 'password2': '0000'})
        self.assertTrue(self.c.login(username='testUser', password='0000'))
        self.c.logout()


class UserDetailViewTests(TestCase):
    def setUp(self):
        self.c = Client()
        self.test_user = setup_default_user()

    def test_get_user_detail_without_user(self):
        with self.assertRaises(NoReverseMatch):
            reverse('user_detail')

    def test_get_user_detail_with_user(self):
        url = reverse('user_detail', kwargs={'username': self.test_user.username})
        res = self.c.get(url)
        self.assertEqual(res.context['user'], self.test_user)

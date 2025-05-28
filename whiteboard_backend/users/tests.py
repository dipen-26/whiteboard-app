from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken

class UserAuthTests(APITestCase):

    def setUp(self):
        self.owner = CustomUser.objects.create_user(username='owneruser', password='ownerpass', role='owner')
        self.editor = CustomUser.objects.create_user(username='editoruser', password='editorpass', role='editor')
        self.viewer = CustomUser.objects.create_user(username='vieweruser', password='viewerpass', role='viewer')

    def get_token_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_register_user(self):
        url = reverse('register')
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpass123',
            'role': 'viewer'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CustomUser.objects.filter(username='newuser').exists())

    def test_unauthorized_access(self):
        url = reverse('secure')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_access(self):
        url = reverse('secure')
        token = self.get_token_for_user(self.owner)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("authenticated", response.data.get('message', '').lower())

    def test_role_based_access_owner(self):
        url = reverse('owner')
        token = self.get_token_for_user(self.owner)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("owner", response.data.get('message', '').lower())

    def test_role_based_access_editor(self):
        url = reverse('editor')
        token = self.get_token_for_user(self.editor)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("editor", response.data.get('message', '').lower())

    def test_role_based_access_viewer(self):
        url = reverse('viewer')
        token = self.get_token_for_user(self.viewer)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("viewer", response.data.get('message', '').lower())

    def test_role_based_access_denied(self):
        # Owner trying to access editor endpoint
        url = reverse('editor')
        token = self.get_token_for_user(self.owner)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

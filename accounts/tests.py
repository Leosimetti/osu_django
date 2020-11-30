from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import userProfile


# test the user registration endpoint
class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {"username": "lynn", "password": "PASwwordLit", "email": "lynn@gmail.com"}
        response = self.client.post('/auth/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# test case for the userprofile model
class userProfileTestCase(APITestCase):
    profile_list_url = reverse('all-profiles')

    def setUp(self):
        # create a new user making a post request to djoser endpoint
        self.user = self.client.post('/auth/users/', data={'username': 'mario', 'password': 'i-keep-jumping'})
        # obtain a json web token for the newly created user
        response = self.client.post('/auth/jwt/create/', data={'username': 'mario', 'password': 'i-keep-jumping'})
        self.token = response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_userprofile_list_authenticated(self):
        response = self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_userprofile_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_userprofile_detail_retrieve(self):
        response = self.client.get(reverse('profile', kwargs={'pk': 1}))
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_userprofile_profile(self):
        profile_data = {'description': 'BIMBO', 'location': 'RUSSIA',
                        'is_creator': 'true', }
        response = self.client.put(reverse('profile', kwargs={'pk': 1}), data=profile_data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

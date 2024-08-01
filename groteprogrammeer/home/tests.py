from django.contrib.auth.models import User
from django.core.asgi import get_asgi_application
from django.core.wsgi import get_wsgi_application
from django.test import TestCase, Client
from django.urls import reverse


# Create your tests here.
class HomeTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        # self.home_url = reverse('home')
        self.user = User.objects.create_user(username='tester', email="tester@gmail.com", password='password')

    def test_awsgi_application(self):
        self.assertIsNotNone(get_asgi_application())
        self.assertIsNotNone(get_wsgi_application())

    def test_index_view_authenticated_user(self):
        # Log in the user
        self.client.login(username='tester', password='password')

        # Test authenticated user is redirected to /home
        response = self.client.get(self.index_url)
        self.assertTemplateUsed(response, "home/home.html")

    def test_index_view_unauthenticated_user(self):
        # Test unauthenticated user sees the index template
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

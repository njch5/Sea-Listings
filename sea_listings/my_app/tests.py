# from django.test import TestCase
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from my_app.views import home, new_search

# Create your tests here.

# URLs Tests
class TestUrls(SimpleTestCase):

  def test_home_resolves(self):
    url = reverse('home')
    self.assertEquals(resolve(url).func, home)

  def test_new_search_resolves(self):
    url = reverse('new_search')
    self.assertEquals(resolve(url).func, new_search)


# Views Tests

class TestViews(TestCase):

  def setUp(self):
    self.client = Client()
    self.home_url = reverse('home')
  
  def test_home_GET(self):
    response = self.client.get(self.home_url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'base.html')
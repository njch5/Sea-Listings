# from django.test import TestCase
from django.test import SimpleTestCase
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
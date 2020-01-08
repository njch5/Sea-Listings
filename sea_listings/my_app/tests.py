# from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from my_app.views import home, new_search

# Create your tests here.
class TestUrls(SimpleTestCase):

  def test_home_resolves(self):
    url = reverse('home')
    self.assertEquals(resolve(url).func, home)

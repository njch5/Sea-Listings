# from django.test import TestCase
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from my_app.views import home, new_search
from my_app.models import Search

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
    self.new_search = reverse('new_search')
  
  def test_home_GET(self):
    response = self.client.get(self.home_url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'base.html')

  def test_new_search_POST(self):
    search ='lawn chair'

    response = self.client.post(self.new_search, {
      'search': search
    })

    self.assertEquals(response.status_code, 200)


# Model Tests

class SearchModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    Search.objects.create(search='keyboard')
  
  def test_search_label(self):
    search = Search.objects.get(id=1)
    field_label = search._meta.get_field('search').verbose_name
    self.assertEquals(field_label, 'search')
  

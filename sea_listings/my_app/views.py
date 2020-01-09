import requests
# It will automatically put a plus or %20 between a space
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup
from . import models

BASE_URL = 'https://seattle.craigslist.org/search/?query={}'

# Create your views here.
def home(request):
  return render(request, 'base.html')

def new_search(request):
  # Pull date from the search bar
  # Python dictionary 'get'
  search = request.POST.get('search')
  # Creates Search object and adds to database
  models.Search.objects.create(search=search)
  final_url = BASE_URL.format(quote_plus(search))
  response = requests.get(final_url)
  data = response.text

  stuff_for_frontend = {
    'search': search,
    }
  return render(request, 'my_app/new_search.html', stuff_for_frontend)
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
  soup = BeautifulSoup(data, features='html.parser')
  # Find all the links that are result-title
  # post_titles = soup.find_all('a', {'class': 'result-title'})

  post_listings = soup.find_all('li', {'class': 'result-row'})
 
  final_postings = []

  for post in post_listings:
    post_title = post.find(class_='result-title').text
    post_url = post.find('a').get('href')
    
    if post.find(class_='result-price'):
      post_price = post.find(class_='result-price').text
    else:
      post_price = 'N/A'

    final_postings.append((post_title, post_url, post_price))

  stuff_for_frontend = {
    'search': search,
    'final_postings': final_postings,
    }
  return render(request, 'my_app/new_search.html', stuff_for_frontend)
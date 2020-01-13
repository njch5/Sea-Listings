import requests
# It will automatically put a plus or %20 between a space
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup
from . import models
from re import sub
from decimal import Decimal

BASE_URL = 'https://seattle.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

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
      # Convert price to decimal/value so we can sort by price
      mon = post.find(class_='result-price').text
      post_price = Decimal(sub(r'[^\d.]', '', mon))
    else:
      post_price = 'N/A'
    
    if post.find(class_='result-image').get('data-ids'):
      post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
      post_image_url = BASE_IMAGE_URL.format(post_image_id)
      print(post_image_url)
    else:
      post_image_url = 'https://craigslist.org/images/peace.jpg'

    final_postings.append((post_title, post_url, post_price, post_image_url))

  selected = request.POST.get('selected')
  # print(selected)
  # print(type(selected))

  ## Next to do: Use Regex to grab digits after $ and before comma

  if selected == '1':
    final_postings = sorted(final_postings, key=lambda x: x[2])
  elif selected == '2':
    final_postings = sorted(final_postings, key=lambda x: x[2], reverse=True)

  # print(final_postings)

  stuff_for_frontend = {
    'search': search,
    'final_postings': final_postings,
    }
  return render(request, 'my_app/new_search.html', stuff_for_frontend)
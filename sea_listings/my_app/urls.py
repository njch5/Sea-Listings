from django.urls import path
from . import views

urlpatterns = [
  # Run the home function from views.py file
  path('', views.home, name='home'),
  # path('admin/', admin.site.urls)
]
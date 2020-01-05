from django.db import models

# Create your models here.

# Created a model called Search with a field called search
class Search(models.Model):
  search = models.CharField(max_length=500)
  created = models.DateTimeField(auto_now=True)

  # Adds an e with search so it's properly plural-ed
  # Column in models/databases
  class Meta:
    verbose_name_plural = 'Searches'
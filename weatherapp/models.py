from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cities(models.Model):
	City_name = models.CharField(max_length = 200,blank=False)


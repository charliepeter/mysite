from django.db import models
import datetime

class TestPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, default=datetime.datetime.now())
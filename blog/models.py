from django.db import models

# Create your models here.
from django.contrib import admin

class entries(models.Model):
	#id: default django will create it
	#id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=50,unique=True)
    title = models.CharField(max_length=100)
    markdown = models.TextField()
    html = models.TextField()
    published = models.DateField()
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


		


from django.db import models

# Create your models here.

# Model shorcut can be used

class MovieRelease(models.Model):

    title = models.CharField(max_length=50)
    studio = models.CharField(max_length=25)
    release_date = models.DateTimeField()
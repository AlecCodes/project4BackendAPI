from django.db import models

# Create your models here.
class Run(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    dur = models.IntegerField(default=0)
    distance = models.IntegerField(default = None, blank = True, null = True)
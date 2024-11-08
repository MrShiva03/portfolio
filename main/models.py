from django.db import models

# Create your models here.

class Project(models.Model):
    image=models.ImageField(blank=True)
    title=models.CharField(max_length=50, blank=True)
    link = models.URLField(blank=True, null=True)
    description=models.CharField(max_length=50, blank=True)

    
class Skill(models.Model):
    name=models.CharField(max_length=25, blank=True)
    percent=models.IntegerField(blank=True, default=50)
    des=(models.CharField(max_length=70, blank=True))

class Certificate(models.Model):
    image=models.ImageField(blank=True)
    title=models.CharField(max_length=50, blank=True)
    description=models.CharField(max_length=50, blank=True)
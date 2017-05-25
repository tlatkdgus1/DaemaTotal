from django.db import models

class VirusModel(models.Model):
    file = models.FileField(null=True,upload_to='file/')

class VirusString(models.Model):
    string = models.TextField(default='')

class VirusFunction(models.Model):
    function = models.TextField(default='')

class VirusDatabase(models.Model):
    hash = models.TextField(default='')
    string = models.ManyToManyField(VirusString)
    function = models.ManyToManyField(VirusFunction)
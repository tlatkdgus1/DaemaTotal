from django.db import models

class VirusModel(models.Model):
    title = models.TextField(default='')
    file = models.FileField(null=True,upload_to='file/')


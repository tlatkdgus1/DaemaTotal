from django.db import models

class VirusModel(models.Model):
    file = models.FileField(null=True,upload_to='file/')


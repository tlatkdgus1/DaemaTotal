from django.db import models

class VirusModel(models.Model):
    file = models.FileField(null=True,upload_to='file/')

class Signature_sha256(models.Model):
    hash = models.TextField(default='')

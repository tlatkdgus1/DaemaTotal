from django.contrib import admin
from .models import VirusModel
from .models import Signature_sha256


admin.site.register(VirusModel)
admin.site.register(Signature_sha256)
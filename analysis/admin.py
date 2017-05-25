from django.contrib import admin
from .models import VirusModel
from .models import VirusString
from .models import VirusFunction
from .models import VirusDatabase


admin.site.register(VirusModel)
admin.site.register(VirusString)
admin.site.register(VirusFunction)
admin.site.register(VirusDatabase)
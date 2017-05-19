from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^analysisHTML/', include('analysis.urls', namespace='analysisHTML'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


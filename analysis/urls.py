from django.conf.urls import url
from . import views
from django.views.static import serve
from django.contrib.auth.decorators import login_required
from django.conf import settings

urlpatterns = [
    # url(r'^media/(?P<path>.*>$', login_required(serve), {'document_root': settings.MEDIA_ROOT}),
    url(r'^index/$', views.Index.as_view(), name='index'),
    url(r'^upload/$', views.UploadVirus.as_view(), name='upload')

]


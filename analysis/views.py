from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic import View
from django.utils import timezone
from .forms import UploadFileForm

from django.contrib.auth import authenticate, login, logout as _logout

class Index(TemplateView):
	template_name='analysisHTML/index.html'

class UploadVirus(View):
    def get(self, request, *args, **kwargs):
        form = UploadFileForm()
        return render(request, 'analysisHTML/upload.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')

from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
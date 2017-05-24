import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import UploadFileForm
from analysis.string_pkg import string
from analysis.virus_pkg import virus
from analysis.virus_pkg import virus_analysis


path_file = "/mnt/c/Users/Sim/PycharmProjects/DaemaTotal/media/file/"

def get_pathFile():
    global path_file
    return path_file

class UploadVirus(View):
    def get(self, request, *args, **kwargs):
        form = UploadFileForm()
        return render(request, 'analysisHTML/index.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UploadFileForm(request.POST, request.FILES)
        extension = os.path.splitext(str(request.FILES.get('file')))[1]

        if extension in '.exe' and form.is_valid():
            form.save()
            filepath = str(path_file+str(request.FILES.get('file')))

            virus_analysis.virus.set_file(filepath)
            string.set_strings()

            virus_analysis.analysis()


            return HttpResponse("Goood")
        return HttpResponse("EXE FILE Please")

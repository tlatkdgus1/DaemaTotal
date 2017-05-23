from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .forms import UploadFileForm
from .virus_info import *
import os
path_file = "/mnt/c/Users/Sim/PycharmProjects/DaemaTotal/media/file/"


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

            set_filePath(filepath)
            set_pe()
            print(get_import())
            get_strings()
            return HttpResponse("Goood")
        return HttpResponse("EXE FILE Please")

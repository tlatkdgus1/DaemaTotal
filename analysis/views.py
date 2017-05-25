import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import UploadFileForm
from analysis.function_pkg import function
from analysis.string_pkg import string
from analysis.virus_pkg import virus_settings
from analysis.virus_pkg import virus_analysis
from analysis.virus_pkg import virus_info
from analysis.virus_pkg import virus
from analysis.virus_pkg.virus_detection.detect_signature import signature_get


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

            virus_analysis.virus_settings.set_file(filepath)
            string.set_strings()

            dict = {
                'dlls' : virus_info.get_dll(),
                'isVirus' : virus.virus_check(),
                'filename' : virus_settings.get_fileName(),
                'warnings' : function.function_warning(),
                'sha256' :signature_get.get_sha256(),
                'textbss' : virus_info.get_section(0),
                'text' : virus_info.get_section(1),
                'rdata': virus_info.get_section(2),
                'data': virus_info.get_section(3),
                'idata': virus_info.get_section(4),
                'gfids': virus_info.get_section(5),
                '00cfg': virus_info.get_section(6),
                'rsrc': virus_info.get_section(7),
                'reloc': virus_info.get_section(8),
            }

            return render(request, 'analysisHTML/result.html', {'dict': dict})
        return HttpResponse("EXE FILE Please")

import pefile
import os

file = ""
pe = ""

def set_file(filepath):
    global file
    file = filepath
    set_pe()

def get_file():
    global file
    return file

def get_fileName():
    global file
    split_file = os.path.split(file)
    return split_file[1]

def get_filePath():
    global file
    split_file = os.path.split(file)
    return split_file[0]

def set_pe():
    global pe
    pe = pefile.PE(file)

def get_pe():
    global pe
    return pe

def virus_check():
   if virus_analysis.analysis_signature():
       return "THIS IS VIRUS"

   return "THIS IS NOT VIRUS"
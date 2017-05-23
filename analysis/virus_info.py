import pefile
import math
import subprocess
from . import string_util

file = ""
pe = ""

def set_filePath(filepath):
    global file
    file = filepath

def set_pe():
    global pe
    pe = pefile.PE(file)

def get_dump():
    return pe.dump_info()

def get_hash():
    for sect in pe.sections:
        print (sect.Name)
        print (sect.get_hash_md5())
        print (sect.get_hash_sha256())

def get_entropy(data):
    if not data:
        return 0

    entropy = 0
    for x in range(256):
        p_x = float(data.count(chr(x)))/len(data)
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)

    return entropy

def get_packing():
    pass

def get_import():
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        print (entry.dll)
    for imp in entry.imports:
        print ('\t', hex(imp.address), imp.name)

def get_strings():
    strings = subprocess.check_output('strings '+file, shell=True).decode('utf-8')
    string_util.set_strings(strings)
    print(string_util.check_ip())
    print(string_util.check_url())
    print(string_util.check_string())



import pefile
import math
from . import virus_settings

def get_dump():
    return virus_settings.get_pe().dump_info()

def get_hash():
    for sect in virus_settings.get_pe().sections:
        print (sect.Name)
        print (sect.get_hash_md5())
        print (sect.get_hash_sha256())

def get_section(num):
    pe = virus_settings.get_pe()
    for i in pe.sections:
        print(i)
    section = pe.sections[num]
    return_dict = {
        'name' : section.Name,
        'vir_addr' : hex(section.VirtualAddress),
        'vir_size' : section.Misc_VirtualSize,
        'raw_size' : section.SizeOfRawData,
        'md5' : section.get_hash_md5(),
    }

    return return_dict

def get_entropy(data):
    if not data:
        return 0

    entropy = 0
    for x in range(256):
        p_x = float(data.count(chr(x)))/len(data)
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)

    return entropy

def get_dll():
    dll_list=[]
    for entry in virus_settings.get_pe().DIRECTORY_ENTRY_IMPORT:
        dll = str(entry.dll).split("b'")
        dll = dll[1].split("'")
        dll = dll[0]
        dll_list.append(dll)

    return dll_list

def get_arch():
    if virus_settings.get_pe().FILE_HEADER.Machine == 0x14c:
        return 32
    else:
        return 64




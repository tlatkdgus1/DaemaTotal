# signature compare to .text section (code section)
import pefile
from analysis.virus_pkg import virus_settings

def get_sha256():
    pe = virus_settings.get_pe()
    virus_hash = pe.sections[0].get_hash_sha256()
    return virus_hash

def get_sha1():
    pe = virus_settings.get_pe()
    virus_hash = pe.sections[0].get_hash_sha1()
    return virus_hash

def get_md5():
    pe = virus_settings.get_pe()
    virus_hash = pe.sections[0].get_hash_md5()
    return virus_hash





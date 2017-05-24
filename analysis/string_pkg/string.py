import subprocess

from analysis.string_pkg import string_util
from analysis.virus_pkg import virus

strings=""

def set_strings():
    global strings
    strings = subprocess.check_output('strings '+virus.get_file(), shell=True).decode('utf-8')
    string_util.set_strings(strings)

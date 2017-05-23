import subprocess

from analysis.string_pkg import string_util

strings=""

def set_strings(file):
    global strings
    strings = subprocess.check_output('strings '+file, shell=True).decode('utf-8')
    string_util.set_strings(strings)
    print (string_util.check_url())
    print (string_util.check_ip())

def check_upx():
    pass
import os
from analysis.string_pkg import string_util
from analysis.string_pkg import string
from analysis.virus_pkg import virus

def upx_unpack():
    if string_util.check_string("UPX"):
        os.system("upx -d -q -o "+virus.get_filePath()+"/unpack_"+virus.get_fileName()+" "+virus.get_file())
        virus.set_file(virus.get_filePath()+"/unpack_"+virus.get_fileName())
        string.set_strings()
        return "UPX"

    return False
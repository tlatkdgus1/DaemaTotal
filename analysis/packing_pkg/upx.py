import os
from analysis.string_pkg import string_util
from analysis.string_pkg import string
from analysis.virus_pkg import virus_settings

def upx_unpack():
    if string_util.check_string("UPX"):
        os.system("upx -d -q -o " + virus_settings.get_filePath() + "/unpack_" + virus_settings.get_fileName() + " " + virus_settings.get_file())
        virus_settings.set_file(virus_settings.get_filePath() + "/unpack_" + virus_settings.get_fileName())
        string.set_strings()
        return "UPX"

    return False
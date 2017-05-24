from analysis.string_pkg import string
from analysis.packing_pkg import packing
from analysis.virus_pkg.virus_detection.detect_signature import signature
from . import virus_settings

def analysis_packing():
    return packing.check_packing()

def analysis_string():
    string_list=[]
    string_list.append(string.string_util.check_url())
    string_list.append(string.string_util.check_ip())

    return string_list

def analysis_signature():
    if signature.signature_sha256()[0]:
        return signature.signature_sha256()

    return False


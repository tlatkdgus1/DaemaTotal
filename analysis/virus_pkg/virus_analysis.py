from analysis.string_pkg import string
from analysis.packing_pkg import packing
from analysis.virus_pkg.virus_detection.detect_signature import signature
from analysis.virus_pkg.virus_detection.detect_heuristic import heuristic
from analysis.function_pkg import function
from . import virus_settings

def analysis_packing():
    return packing.check_packing()


def analysis_signature():
    if signature.signature_sha256()[0]:
        return signature.signature_sha256()

    return False

def analysis_heuristic():
    heuristic.heuristic()


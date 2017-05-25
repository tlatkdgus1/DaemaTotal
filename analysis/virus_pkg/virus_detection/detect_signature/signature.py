# signature compare to .text section (code section)
from . import signature_compare

def signature_sha256():
    return signature_compare.signature_compare()


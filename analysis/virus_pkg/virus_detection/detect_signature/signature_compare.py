from analysis.models import Signature_sha256
from . import signature_get
from analysis.virus_pkg import virus_settings
def signature_compare():
    signature = Signature_sha256.objects.all()
    return_list = []
    for sig in signature:
        if sig.hash == signature_get.get_sha256():
            return_list.append(True)
            return_list.append(virus_settings.get_pe())

            return return_list
    return_list.append(False)
    return return_list

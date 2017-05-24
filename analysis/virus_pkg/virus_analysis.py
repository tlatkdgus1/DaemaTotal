from analysis.string_pkg import string
from analysis.packing_pkg import packing
from . import virus
def analysis():

    print(string.string_util.check_url())
    print(string.string_util.check_ip())
    print(packing.check_packing())
    print(string.string_util.check_url())
    print(string.string_util.check_ip())

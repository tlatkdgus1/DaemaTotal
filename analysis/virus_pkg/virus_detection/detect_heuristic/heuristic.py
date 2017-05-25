from . import heuristic_compare

def heuristic():
    print (str(heuristic_compare.get_percent()))
    if (int(heuristic_compare.get_percent()) > 10):
        return True
    return False
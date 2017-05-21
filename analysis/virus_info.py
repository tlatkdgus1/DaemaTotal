import pefile

def get_dump(filename):
    pe = pefile.PE(filename)
    return pe.dump_info()


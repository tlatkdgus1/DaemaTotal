from analysis.virus_pkg import virus_settings

def get_function():
    function=[]
    for entry in virus_settings.get_pe().DIRECTORY_ENTRY_IMPORT:
        for imp in entry.imports:
            imp = str(imp.name).split("b'")
            imp = imp[1].split("'")
            imp = imp[0]
            function.append(imp)

    return function
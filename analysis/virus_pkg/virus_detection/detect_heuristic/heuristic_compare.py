from analysis.string_pkg import string_util
from . import heuristic_get
from analysis.models import VirusDatabase

virus_database = VirusDatabase.objects.all()

def get_percent():
    return compare_string()+compare_function()

def compare_string():
    string_match=0
    string_count=0
    strings = heuristic_get.heuristic_string()

    for virus in virus_database:
        virus_strings = virus.string.all()
        for virus_string in virus_strings:
            for string in strings:
                if virus_string.string == string:
                    string_match = string_match+1
    for string in strings:
        string_count = string_count+1

    if(string_match > 0):
        return (string_match / string_count)*100

    return 0


def compare_function():
    function_match = 0
    function_count = 0
    functions = heuristic_get.heuristic_function()

    for virus in virus_database:
        virus_functions = virus.function.all()
        for virus_function in virus_functions:
            for function in functions:
                print(virus_function.function+" : "+function)
                if virus_function.function == function:
                    function_match = function_match + 1
    for function in functions:
        function_count = function_count + 1

    if (function_match > 0):
        return (function_match / function_count) * 100

    return 0

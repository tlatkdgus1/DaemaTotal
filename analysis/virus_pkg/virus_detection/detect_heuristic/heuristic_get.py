from analysis.string_pkg import string_util
from analysis.function_pkg import function_get

def heuristic_string():
    global string_count
    heuristic_list=[]
    string_list = string_util.check_url()
    for string in string_list:
        heuristic_list.append(string)

    string_list = string_util.check_ip()
    for string in string_list:
        heuristic_list.append(string)

    return heuristic_list

def heuristic_function():
    function_list =  function_get.get_function()
    return function_list
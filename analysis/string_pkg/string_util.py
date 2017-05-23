import re

strings=""
return_tuple=[]
return_value=""

def set_strings(strings1):
    global strings
    strings = strings1.split("\n")

def check_ip():
    global strings
    return_tuple=[]
    pattern = re.compile("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(:[0-9]+)?$")

    for i in strings:
        string = pattern.match(i)
        if string:
            return_tuple.append(string.group())

    return return_tuple

def check_url():
    global strings
    return_tuple = []
    pattern1 = re.compile("^(file|gopher|news|nntp|telnet|https?|ftps?|sftp):\/\/([^:\/\s]+)(:([^\/]*))?((\/[^\s/\/]+)*)?\/?([^#\s\?]*)(\?([^#\s]*))?(#(\w*))?$")
    pettern2 = re.compile("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(:[0-9]+)?\/([^:\/\s]+)(:([^\/]*))?((\/[^\s/\/]+)*)?\/?([^#\s\?]*)(\?([^#\s]*))?(#(\w*))?$")

    for i in strings:
        string = pattern1.match(i)
        if string:
            return_tuple.append(string.group())
        else:
            string = pettern2.match(i)
            if string:
                return_tuple.append(string.group())

    return return_tuple

def check_upx():
    global strings
    pattern = re.compile("UPX0")

    for i in strings:
        string = pattern.match(i)
        if string:
            return True

    return False

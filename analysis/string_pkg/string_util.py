import re

strings=""
return_value=""

def set_strings(strings1):
    global strings
    strings = strings1.split("\n")

def get_strings():
    global strings
    return strings

def check_ip():
    global strings
    return_list=[]
    pattern = re.compile("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(:[0-9]+)?$")

    for i in strings:
        string = pattern.match(i)
        if string:
            return_list.append(string.group())

    return return_list

def check_url():
    global strings
    return_list = []
    pattern1 = re.compile("^(file|gopher|news|nntp|telnet|https?|ftps?|sftp):\/\/([^:\/\s]+)(:([^\/]*))?((\/[^\s/\/]+)*)?\/?([^#\s\?]*)(\?([^#\s]*))?(#(\w*))?$")
    pettern2 = re.compile("^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(:[0-9]+)?\/([^:\/\s]+)(:([^\/]*))?((\/[^\s/\/]+)*)?\/?([^#\s\?]*)(\?([^#\s]*))?(#(\w*))?$")

    for i in strings:
        string = pattern1.match(i)
        if string:
            return_list.append(string.group())
        else:
            string = pettern2.match(i)
            if string:
                return_list.append(string.group())

    return return_list

def check_string(string):
    global strings
    pattern = re.compile(string)

    for i in strings:
        string = pattern.match(i)
        if string:
            return True

    return False

import re

strings=""

def set_strings(strings1):
    global strings
    strings = strings1

def check_ip():
    global strings
    pattern = re.compile("^(?:(?:25[0 - 5] | 2[0 - 4][0 - 9] | [01]?[0 - 9][0 - 9]?)\.){3}(?:25[0 - 5] | 2[0 - 4][0 - 9] | [01]?[0 - 9][0 - 9]?)$")
    string = pattern.match(strings)
    if string:
        return string.group()
    else:
        return None

def check_url():
    global strings
    pattern = re.compile("/^(file|gopher|news|nntp|telnet|https?|ftps?|sftp):\/\/([a-z0-9-]+\.)+[a-z0-9]{2,4}.*$/")
    string = pattern.match(strings)
    if string:
        return string.group()
    else:
        return None

'''
def check_string(strings):
    print (strings)
    pattern = re.compile("Hello")
    string = pattern.match("Helo world")

    if string:
        return string.group()
    else:
        return None
'''
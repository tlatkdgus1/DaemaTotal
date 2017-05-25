from . import function_get

func_warning=["OpenProcess", "VirtualAllocEx", "WriteProcessMemory", "LoadLibraryA","system",
              "CreateRemoteThread", "RegCreateKeyExA", "RegSetValueExA", "Keybd_event", "Mouse_event",
              "CreateFileA", "Shellexecute", "WinExec", "FtpOpenFile", "WriteFile", "ReadFile",
              "CreateProcessA"]

def function_compare():
    warning_list=[]
    func_list = function_get.get_function()

    for func in func_list:
        for warning in func_warning:
            if warning == func:
                warning_list.append(func)

    return warning_list
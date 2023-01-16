"""
This script uses the psutil.process_iter() function to iterate through all running processes on the machine.
It filters the processes that are running under the svchost.exe process, as most of the services run under this process.
It then appends all the services running under svchost.exe to a list and prints it out at the end.

Please note that this script will only work on Windows and it uses the as_dict method which is only available in version 5.4.0 and higher of psutil.
Also, the script relies on the name of the process, so if the service is running under a different process name or if the service is not running under svchost.exe it will not show up in the list.
"""

import psutil

services = []
for process in psutil.process_iter():
    try:
        pinfo = process.as_dict(attrs=['pid', 'name', 'create_time'])
        if pinfo['name'] == 'svchost.exe':
            for i in process.children(recursive=True):
                services.append(i.name())
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

print("Services running:")
for service in services:
    print(service)
# This script uses the psutil.process_iter() function to iterate through all running processes on a Windows system.
# It will analyse the processes that are running under the svchost.exe process, and print it out at the end.
# Svchost.exe, or Service Host, is an important Windows process hosting one or more Windows services. "
# - "It allows Windows to group a number of services in a single process, thus reducing resource consumption."
# - source: https://nordvpn.com/blog/what-is-svchost-exe/
# This script is for Windows only and the as.dict method only works in Python 5.4.0
# V1.0 NP

import psutil

services = []
for process in psutil.process_iter():
    try:
        # gather the processes - process id, name and time created (3 peices of data)
        # convert the dataclass to a dictionary using as_dict (dictionaries in Python are a specific dynamic data structure (no size))
        # we can store all the process data in one object - pinfo 
        pinfo = process.as_dict(attrs=['pid', 'name', 'create_time'])
        if pinfo['name'] == 'svchost.exe':
            for i in process.children(recursive=True):
                services.append(i.name())
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
# print out which ones are running
print("Services running:")
for service in services:
    print(service)

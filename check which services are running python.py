# This script uses the psutil.process_iter() function to iterate through all running processes on a windows system.
# It will analyse the processes that are running under the svchost.exe process, and print it out at the end.
# This script is for Windows only and the as.dict method only works in Python 5.4.0
# V1.0 NP

import psutil

services = []
for process in psutil.process_iter():
    try:
        #gather the processes - process id, name and time created
        pinfo = process.as_dict(attrs=['pid', 'name', 'create_time'])
        if pinfo['name'] == 'svchost.exe':
            for i in process.children(recursive=True):
                services.append(i.name())
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
#print out which ones are running
print("Services running:")
for service in services:
    print(service)

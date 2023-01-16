# This python script is used in emergencies if you anticipate a hacker is in the system and you want to kill off any open doors immediately.
# lsof command descrption: "The lsof (list open files) command returns the user processes that are actively using a file system." 
# -source: https://www.ibm.com/docs/en/spectrum-scale/5.1.0?topic=commands-lsof-command
# It will list all processes thet are listening on a open port and then kill them off using the kill -9 command 
# (the kill command is used to kill processes in linux and -9 will forcefully kill off the process without question).
# Be careful with this one as it will kill off all listening ports without giving you a chance to finish off any transfers or activities in action etc.
# V1.0 NP

import os

def close_ports():
    command = "lsof -i -n -P | grep LISTEN | awk '{print $2}' | xargs kill -9"
    os.system(command)

close_ports()

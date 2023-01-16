# This python script is used in emergencies if you anticipate a hacker is in the system and you want to kill off any open doors immediately.
# This script will utilise the lsof command - the lsof command stands for LiSt Open Files and shows open files and which process uses them.
# It will list all processes thet are listening on a open port and then kill them off using the kill -9 command.
# Be careful with this one as it will kill off all listening ports without giving you a chance to finish off any transfers etc.
# V1.0 NP

import os

def close_ports():
    command = "lsof -i -n -P | grep LISTEN | awk '{print $2}' | xargs kill -9"
    os.system(command)

close_ports()

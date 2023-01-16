# This script is if you suspect your passwd/shadow file have been compromised and its time to reset everyones passwords on the system!
# This script will use the command - chage. What is chage? description below:
# "One of the helpful tools in Linux is the “chage” command. From its name, the “chage” command is derived from the words “Change Age”
# - which is used to modify the information such as duration when to change password, make account status active or inactive, sets expiry date of the account
# - and sets a reminder to change the password through an alarm before user’s account will be inactive." - source: https://linuxhint.com/use-linux-chage-command/
# chage is used here to change the password aging info of all users on a linux system.
# It sets the number of days since January 1st, 1970 that the users password was last changed to a factor of 0. Ultimately forcing them to change it when they next login.
# Warning: it will do it for the root account also - so be careful using this
# V1.0 NP

import subprocess

def change_password():
    command = "chage -d 0 $(awk -F: '{print $1}' /etc/passwd)"
    subprocess.run(command, shell=True)

change_password()

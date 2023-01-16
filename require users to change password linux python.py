"""
This script will execute shell command chage -d 0 $(awk -F: '{print $1}' /etc/passwd) using subprocess.run().
This command will change the password aging information for all users on the system, specifically it will set the number of days since January 1st, 1970 that the user's password was last changed to 0.
This will trigger the system to prompt the user to change their password the next time they try to login.

It is worth noting that this script will change the password aging information for all users on the system, including the root user. It is also worth noting that the users will be prompted to change the password on their next login.

This script should be run with caution, as it could cause issues if the user is not able to change their password. It is also recommended to notify all the users before running this script.
"""
import subprocess

def change_password():
    command = "chage -d 0 $(awk -F: '{print $1}' /etc/passwd)"
    subprocess.run(command, shell=True)

change_password()
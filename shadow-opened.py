# This is a short script which will search the auth log file in linux to determine if anyone has opened
# This will give an indication as to whether it was opened - which indicates a concern for user account security
# You can modify the location of the log file if your using another iteration of unix/linux
# V1.0 NP
import re

log_file = '/var/log/auth.log'

with open(log_file, 'r') as f:
    log_data = f.read()

shadow_opened = re.search(r'/etc/shadow.*opened', log_data)

if shadow_opened:
    print('The /etc/shadow file was opened - this is bad sign.')
else:
    print('The /etc/shadow file was not opened - user passwords likely are safe.')

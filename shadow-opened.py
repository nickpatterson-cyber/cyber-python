# This is a short script which will search the auth log file in linux to determine if anyone has opened it
# This will give an indication about concerns for user account security
# You can modify the location of the log file if your using another iteration of unix/linux - I am using /var/log/auth.log for this example
# You could also use /var/log/syslog or /var/log/messages
# V1.0 NP

import re
# system log file
log_file = '/var/log/auth.log'

# open the log file
with open(log_file, 'r') as f:
    log_data = f.read()
    
# run a search
shadow_opened = re.search(r'/etc/shadow.*opened', log_data)

# if the file has been opened alter the operator - otherwise give a safety message
if shadow_opened:
    print('The /etc/shadow file was opened - this is bad sign.')
else:
    print('The /etc/shadow file was not opened - user passwords likely are safe.')

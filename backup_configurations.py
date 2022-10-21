#Backup of configuration

import netmiko
import os

device1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}

#Change directory
os.chdir('/home/cisco/backups')

net_connect = netmiko.ConnectHandler(**device1)

net_connect.enable()

output = net_connect.send_command('show run')

#Print device output to screen
print(output)

#Create backup file
#Filename = device hostname + current date/time

filename = str(net_connect.base_prompt) + '_' + str(net_connect.find_prompt()[:15])

#Create and open backup file

backup_file = open(filename, 'w')

#Write device output to file

backup_file.write(output)

#Close backup file

backup_file.close()
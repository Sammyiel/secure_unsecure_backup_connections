#Secure remote connection

import netmiko

device1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco'
}

net_connect = netmiko.ConnectHandler(**device1)

net_connect.enable()

print(net_connect.find_prompt())

#!/usr/bin/env python3

from netmiko import ConnectHandler
from getpass import getpass

# Prompt for username and password
username = input("Username: ")
password = getpass()
device = input("What node are you configuring? ")

# node aka router or switch connection information
node = {
'device_type': 'cisco_ios',
'host': device,
'username': username,
'password': password
}

# establish connection
ssh = ConnectHandler(**node)

# desired configuration set
configuration = [ 
    'interface {{ interface }}',
    'description {{ description }}', 
    'ip address {{ ip address }} {{ subnet mask }}'
]

# push configuration set to the node
ssh.send_config_set(configuration)

# inform user of completion 
print("The interface has been configured")

# disconnect from node
ssh.disconnect()

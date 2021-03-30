from netmiko import ConnectHandler
from getpass import getpass

# Prompt for username and password
username = input("Username: ")
password = getpass()

# node aka router or switch connection information
node = {
'device_type': 'cisco_ios',
'host': 'ip address or hostname',
'username': username,
'password': password
}

# establish connection
connect = ConnectHandler(**node)

# desired configuration set
configuration = [
    'conf t', 
    'int lo 0', 
    'ip address x.x.x.x 255.255.255.255'
]

# push configuration set to the node
connect.send_config_set(configuration=node)

# inform user of completion 
print("The interface has been configured")

# disconnect from node
node.disconnect()

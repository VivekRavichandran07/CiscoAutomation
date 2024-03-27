from netmiko import ConnectHandler
from datetime import datetime
import getpass
#import logging
#logging.basicConfig(filename='test.log', level=logging.DEBUG)
#logger = logging.getLogger("netmiko")

print('!!! SSH Access-list configuration !!!')

with open('devices.txt') as f:
    devices = f.read().splitlines()

device_list = list()

username = input('Enter the username: ')
password = getpass.getpass('Enter the password: ')
secret = getpass.getpass('Enter the enable password: ')

for ip in devices:
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': username,
        'password': password,
        'secret': secret,
        'port': 22,
        }
    device_list.append(cisco_device)

for device in device_list:  
    connection = ConnectHandler(**device)

    print(f'Connected to the device: {device["host"]}')
       
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    prompt = connection.find_prompt()
    hostname = prompt[0: -1]
    print(hostname)

    check_enable_mode = connection.check_enable_mode()
    print(f'The device is in enable mode: {check_enable_mode}')
    if not check_enable_mode is True:
        connection.enable()
        
    filename = f'{hostname}_{month}_{day}_{year}_{hour}:{minute}-pre_backup.txt'
    pre_config_backup = connection.send_command('show run') 

    with open(filename, 'w') as backup:
        backup.write(pre_config_backup)
        print('*' * 50)
        print(f'Pre_Backup of {hostname} completed succesfully')
        print('*' * 50)

    check_config_mode = connection.check_config_mode()
    if not connection.check_config_mode():
        connection.config_mode()
    
    output = connection.send_config_from_file('config.txt') # use Input function to prompt for different config for each router.
    print(output)

    filename = f'{hostname}_{month}_{day}_{year}_{hour}:{minute}-post_backup.txt'
    post_config_backup = connection.send_command('show run') 
    with open(filename, 'w') as backup:
        backup.write(post_config_backup)
        print('*' * 50)
        print(f'Post_Backup of {hostname} completed succesfully')
        print('*' * 50)

    print(f'Closing connection to {device["host"]}')
    print('+' * 70)
    connection.disconnect()
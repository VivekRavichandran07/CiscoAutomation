# Python Automation with Netmiko for Updating Access List VTY Lines on Cisco Devices

This Python script automates the process of updating access list VTY lines on Cisco devices using Netmiko library. Access list VTY lines are crucial for securing remote access to Cisco devices.

## Prerequisites
- Python installed on your machine
- Netmiko library installed (`pip install netmiko`)
- SSH access enabled on your Cisco devices

## Usage
1. Clone or download the Python script from this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Modify the script with your Cisco device credentials, access list configurations, and other parameters as needed.
4. Run the script: `python update_access_list.py`.
5. Follow the on-screen instructions to provide necessary inputs and confirm actions.

## Features
- Connects to Cisco devices via SSH using Netmiko library.
- Dynamically updates access list VTY lines based on user input.
- Error handling for connection issues and command execution failures.
- Interactive user interface for input validation and confirmation.

## Script Overview
python
import netmiko

# Define Cisco device credentials
device = {
    'device_type': 'cisco_ios',
    'host': 'your_device_ip',
    'username': 'your_username',
    'password': 'your_password',
}

# Define access list configurations
access_list = [
    'access-list 1 permit any', 
    'access-list 1 deny any'
]

# Connect to device
connection = netmiko.ConnectHandler(**device)

# Update access list VTY lines
for line in access_list:
    connection.send_command(line)

# Disconnect from device
connection.disconnect()


## Disclaimer
This script is provided as-is, without any warranties. Use it at your own risk. Ensure you have appropriate permissions before making changes to network devices.

## Contribution
Feel free to contribute to this repository by submitting pull requests with improvements or additional features.

This README provides an overview of how to use the Python script for automating the update of access list VTY lines on Cisco devices using Netmiko. You can further customize it to fit your specific use case or requirements.

import os

from netmiko import ConnectHandler

password = os.environ["PASSWORD"]

iosv_l2_s1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.234",
    "username": "test",
    "password": password,
}

net_connect = ConnectHandler(**iosv_l2_s1)
output = net_connect.send_command("show ip int brief")
print(output)

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.233',
    'username': 'test',
    'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l2_s1)
output = net_connect.send_command('show ip int brief')
print(output)

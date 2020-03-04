from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
	'ip': '192.168.122.80',
	'username': 'steve',
	'password': 'cisco'
}
iosv_l2_s2 = {
    'device_type': 'cisco_ios',
	'ip': '192.168.122.82',
	'username': 'steve',
	'password': 'cisco'
}
iosv_l2_s3 = {
    'device_type': 'cisco_ios',
	'ip': '192.168.122.84',
	'username': 'steve',
	'password': 'cisco'
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
	'ip': '192.168.122.86',
	'username': 'steve',
	'password': 'cisco'
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
	'ip': '192.168.122.88',
	'username': 'steve',
	'password': 'cisco'
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
	'ip': '192.168.122.90',
	'username': 'steve',
	'password': 'cisco'
}

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3, iosv_l2_s4, iosv_l2_s5, iosv_l2_s6]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,11):
        print ("creating VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print(output)
# creates multiple vlans on all switches via ssh        
	
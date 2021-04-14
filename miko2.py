from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios', #dictionary for switch1
	'ip': '192.168.122.80',
	'username': 'steve',
	'password': 'cisco'
}
iosv_l2_s2 = {
    'device_type': 'cisco_ios', #dictionary for switch2
	'ip': '192.168.122.82',
	'username': 'steve',
	'password': 'cisco'
}
iosv_l2_s3 = {
    'device_type': 'cisco_ios', #dictionary for switch3
	'ip': '192.168.122.84',
	'username': 'steve',
	'password': 'cisco'
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios', #dictionary for switch4
	'ip': '192.168.122.86',
	'username': 'steve',
	'password': 'cisco'
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios', #dictionary for switch5
	'ip': '192.168.122.88',
	'username': 'steve',
	'password': 'cisco'
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios', #dictionary for switch6
	'ip': '192.168.122.90',
	'username': 'steve',
	'password': 'cisco'
}

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3, iosv_l2_s4, iosv_l2_s5, iosv_l2_s6] #list of switch dictionarys

for devices in all_devices: #initialise loop through switches
    net_connect = ConnectHandler(**devices) #use netmiko to connect to current device in list
    for n in range (2,11): #initialise loop to send commands to switch
        print ("creating VLAN " + str(n)) #displays which vlan is about to be created
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)] # define a set of configration commands to create vlans
        output = net_connect.send_config_set(config_commands) #send the config commands to creating vlans on current switch in loop
        print(output) #show output
# creates multiple vlans on all switches via ssh        
	

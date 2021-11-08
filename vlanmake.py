# Creates 4 vlans on diffrent switches
# the plain text file 'twitches' contains the ip addresses of the target switches
# This file is opened and assigned to the variable 'f'
# The loop begins by assigning the ip address stored in 'f' to the count variable 'adds'
# The strip command removes any unwanted spaces in 'adds'
# The print command tells the user which switch is being configured
# The telnet library function is assigned to the varible 'tn' and is used to connect to the switch specified in the variable 'adds'
# The telnet library function is used to enter the username and password entered by the user earlier
# The rest of the loop creates the vlans on the target switches by using the telnet library function the send ios commands to the switch
# Not efficient. Same username and password for all switches. Vlans could be created using a loop  
import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your telnet username : ")
password = getpass.getpass()

f = open('twitches')

for adds in f:
    adds=adds.strip()
    print ("configuring switch " + (adds))
    tn = telnetlib.Telnet(adds)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
    tn.write(b"enable\n")
    tn.write(b"conf t\n")
    tn.write(b"vlan 20\n")
    tn.write(b"name twenty\n")
    tn.write(b"vlan 30\n")
    tn.write(b"name thirty\n")
    tn.write(b"vlan 40\n")
    tn.write(b"name fourty\n")
    tn.write(b"vlan 50\n")
    tn.write(b"name fifty\n")   
    tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"exit\n")
    print (tn.read_all().decode('ascii'))





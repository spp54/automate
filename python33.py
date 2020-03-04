import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your telnet username : ")
password = getpass.getpass()

f = open('twitches')

for adds in f:
    adds=adds.strip()
    print ("configuring switch " + (adds))
    HOST = adds
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
    tn.write(b"enable\n")
    tn.write(b"conf t\n")
    tn.write(b"vlan 20\n")
    n.write(b"name twenty\n")
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
# creates four vlans on all six switches




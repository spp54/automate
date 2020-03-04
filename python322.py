import getpass
import telnetlib

HOST = "192.168.122.80"
user = input("Enter your telnet username : ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

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
# creates four vlans
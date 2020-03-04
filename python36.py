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
    
    for n in range(2,10):
        tn.write(b"no vlan " + str(n).encode('ascii') + b"\n")
        tn.write(b"name sw2vlan_" + str(n).encode('ascii') + b"\n")
    
    tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"exit\n")
    print (tn.read_all().decode('ascii'))
# creates multiple vlans using nested loops




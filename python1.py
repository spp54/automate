#This a simple python script to access a router or switch and execute some basic commands
#

import getpass  #import the getpass library module
import telnetlib #import the telnet library

HOST = "192.168.122.71" #Assign the ip address of the device I am going to access to the varible HOST
user = input("Enter your telnet username : ") #Prompt the user to enter I.D and assign it to the varible user
password = getpass.getpass() #Use the getpass module to prompt the user to enter a password and assign it to the variable password

tn = telnetlib.Telnet(HOST) #Use the telnet function in the telnet library to telnet the host and assign this function to the function tn

tn.read_until(b"Username: ") #read the open telnet session until the string 'Username:' is received from the host
tn.write(user.encode('ascii') + b"\n") #write the I.D. entered by the user to the host
if password:
    tn.read_until(b"Password: ") #read the open telnet session until the string 'Password:' is received
    tn.write(password.encode('ascii') + b"\n") # #write the password entered by the user to the host
    
#security has now been passed and a cisco terminal session is now established and commands can be entered.

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"int loop 10\n")
tn.write(b"ip add 1.1.1.1 255.255.255.0\n")
tn.write(b"end\n")
tn.write(b"exit\n")
print tn.read_all().decode('ascii')

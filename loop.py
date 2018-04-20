import getpass
import sys
import telnetlib

HOST = "192.168.192.145"
user = raw_input("Enter your username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST, timeout = 5)

tn.read_until("Username:")
tn.write(user + "\n")

if password:
    tn.read_until("Password:")
    tn.write(password +  "\n")
tn.write("conf t\n")
for i in range (1, 6):
    tn.write("int lo "+ str(i)+ "\n")
    tn.write("ip add " + str(i) + "." + str(i) + "." + str(i) + "." + str(i) +" 255.255.255.255\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()	
 

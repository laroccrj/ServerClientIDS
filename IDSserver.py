#Usage:
#Accepts two arguments
#First is the port to bind to
#Second is the password
#I am not going to do any error checking 
#because we have to type this up again at 
#the competition


import sys
import socket  

port = sys.argv[1]
password = sys.argv[2]
s = socket.socket()
host = socket.gethostname()

s.bing((host, port))
s.listen(5)
c, addr = s.accept()

#To do:
#Get password and authenticate it

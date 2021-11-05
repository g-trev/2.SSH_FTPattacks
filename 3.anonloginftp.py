#
#!/usr/binpython

import ftplib 
import pexpect
from termcolor import colored 

def anonlogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login("anonymous", "anonyomous")		#trys to connect with random creds
		print(colored("[+] ", + hostname, + "FTP anonymous login successful.", "green"))
		ftp.quit()
		return True
	
	except Exception e:
		print(colored("[x] ", + hostname, + " FTP anonymous login failed.", "red"))

host = input("enter the IP address: ")
anonlogin(host)
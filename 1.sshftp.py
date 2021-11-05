#automates ssh login, captures root password, list running processes 

#!/usr/bin/python

import pexpect 	#allows us to automate some of the ssh login

PROMPT = ["#", ">>>", ">", "\$"]

def send_command(child, command):
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
	child.expect(PROMPT)
	return child

def main():
	host = input("enter target host: ")
	user = input("enter ssh username: ")
	password = input("enter ssh password: ")
	child = connect(user, host, password)
	send_command(ssh, "ls;ps") 	#first comands lists etc shadow file then second command lists the root password hash and the processes running on the target system

main()	




















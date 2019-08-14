import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.199.1", port=22, username="becse", password="18978121477", timeout=10)
ssh_shell = ssh.invoke_shell()
cmd = ['configure', 'set interfaces ethernet eth2 address 1.1.1.2/24', 'commit', 'save']

for m in cmd:
    res = ssh_shell.sendall(m+'\n')
    time.sleep(float(1))
ssh.close()

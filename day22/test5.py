# -*- coding: utf-8 -*-
# Author: hkey

import paramiko
hostname = '192.168.118.15'
username = 'root'
password = '123456'
paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()
ssh.load_host_keys()
ssh.connect(hostname=hostname, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command('free -h')
print(stdout.read())
ssh.close()


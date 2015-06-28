# -*- coding: utf-8 -*-
"""It uses the pexpect library to connect to a SSH server using Username,Host Ip
   and password to the user. pexpect is used to automate the process when the situation
   served by the server of the kind:
       
        attacker$ ssh root@127.0.0.1
        
        The authenticity of host '127.0.0.1 (127.0.0.1)' can't be established.
        RSA key fingerprint is 5b:bd:af:d6:0c:af:98:1c:1a:82:5c:fc:5c:39:a3:68.
        
        Are you sure you want to continue connecting (yes/no)? yes
        
        Warning: Permanently added '127.0.0.1' (RSA) to the list of known 
        hosts.
        
        Password:**************
        Last login: Mon Oct 17 23:56:26 2011 from localhost
        attacker:∼ """

"""To start a SSH server in Kali to test the script you could generate SSH keys and start a SSH server by following:
    
    attacker# sshd-generate
    Generating public/private rsa1 key pair.
    <..SNIPPED..>
    attacker# service ssh start
    ssh start/running, process 4376
    attacker# python sshCommand.py
    cat /etc/shadow | grep root
    root:$6$ms32yIGN$NyXj0YofkK14MpRwFHvXQW0yvUid.slJtgxHE2EuQqgD74S/
    GaGGs5VCnqeC.bS0MzTf/EFS3uspQMNeepIAc.:15503:0:99999:7:::"""

import pexpect
PROMPT =['# ', '>>> ', '> ', '\$ ']

def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print child.before

def connect(user, host, password):
    ssh_newkey ='Are you sure you want to continue connecting'
    connStr ='ssh ' +user +'@' +host
    child =pexpect.spawn(connStr)
    ret =child.expect([pexpect.TIMEOUT, ssh_newkey, \
    '[P|p]assword:'])
    if ret ==0:
        print '[-] Error Connecting'
        return
    if ret ==1:
        child.sendline('yes')
        ret =child.expect([pexpect.TIMEOUT, \
        '[P|p]assword:'])
    if ret ==0:
        print '[-] Error Connecting'
        return
    child.sendline(password)
    child.expect(PROMPT)
    return child

def main():
    host ='localhost'
    user ='root'
    password ='toor'
    child =connect(user, host, password)
    send_command(child, 'cat /etc/shadow | grep root')
    
if __name__ =='__main__':
    main()
"""The function returnDefault() takes an FTP connection as the input and 
returns an array of default pages it finds. It does this by issuing the command NLST, 
which lists the directory contents. The function checks each file returned by 
NLST against default web page file names. It also appends any discovered default 
pages to an array called retList. After completing the iteration of these files, 
the function returns this array."""

import ftplib

def returnDefault(ftp):
    try:
        dirList =ftp.nlst()
    except:
        dirList =[]
        print '[-] Could not list directory contents.'
        print '[-] Skipping To Next Target.'
        return
    retList =[]
    for fileName in dirList:
        fn =fileName.lower()
        if '.php' in fn or '.htm' in fn or '.asp' in fn:
            print '[+] Found default page: ' +fileName
            retList.append(fileName)
    return retList

host ='192.168.95.179'
userName ='guest'
passWord ='guest'
ftp =ftplib.FTP(host)
ftp.login(userName, passWord)
returnDefault(ftp)
import os
import optparse
from _winreg import *

def sid2user(sid):
    """ Files in Recycle Bin are named as:
        S-1-5-21-1275210071-1715567821-725345543-1005
        where this SID is for a particular user which can be
        translated by using Registry key:
            HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows  NT\CurrentVersion\ProfileList\<SID>\ProfileImagePath
        Inspecting above key returns us:
            %SystemDrive%\Documents and Settings\<USERID>
        i.e the username."""
        
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,
        "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"
        +'\\' +sid)
        (value, type) =QueryValueEx(key, 'ProfileImagePath')
        user =value.split('\\')[-1]
        return user
    except:
        return sid

def returnDir():
    """This function recovers the Recycle Bin directory on the various Windows OS."""
    
    dirs=['C:\\Recycler\\','C:\\Recycled\\','C:\\$Recycle.Bin\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None
    
def findRecycled(recycleDir):
    dirList =os.listdir(recycleDir)
    for sid in dirList:
        files =os.listdir(recycleDir +sid)
        user =sid2user(sid)
        print '\n[*] Listing Files For User: ' +str(user)
        for file in files:
            print '[+] Found File: ' +str(file)

def main():
    recycledDir =returnDir()
    findRecycled(recycledDir)

if __name__ =='__main__':
    main()
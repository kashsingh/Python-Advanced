import os,random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def encrypt(key,filename):
    chunksize=64*1024
    outputFile="encrypted_"+filename
    filesize=str(os.path.getsize(filename)).zfill(16)       # It will fill the left portion of file name with 0s.
    IV=''
    
    for i in range(16):
        IV+=chr(random.randint(0,0xFF))
        
    encryptor= AES.new(key,AES.MODE_CBC,IV)
    
    with open(filename,'rb') as infile:
        with open(outputFile,'wb') as outfile:
            outfile.write(filesize)
            outfile.write(IV)
            
            while True:
                chunk=infile.read(chunksize)
                
                if len(chunk)==0:
                    break
                elif len(chunk)%16 != 0:
                    chunk+=" "*(16-(len(chunk)%16))
                    
                outfile.write(encryptor.encrypt(chunk))

def decrypt(key,filename):
    chunksize=64*1024
    outputFile=filename[10:]
    
    with open(filename,'rb') as infile:
        filesize=long(infile.read(16))
        IV=infile.read(16)
        
        decryptor= AES.new(key,AES.MODE_CBC,IV)
    
        with open(outputFile,'wb') as outfile:
            while True:
                chunk=infile.read(chunksize)
                
                if len(chunk)==0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)
            
def getKey(password):
    hasher=SHA256.new(password)
    return hasher.digest()
    
def main():
    choice=raw_input("Encrypt or Decrypt ??(E/D) :")
    
    if choice=="E" or choice=="e":
        filename=raw_input("Enter filename :")
        password=raw_input("Enter password :")
        encrypt(getKey(password),filename)
        print "Success!!!"
    
    elif choice=="D" or choice=="d":
        filename=raw_input("Enter filename :")
        password=raw_input("Enter password :")
        decrypt(getKey(password),filename)
        print "Success!!!"
    
    else:
        print "Wrong Input chutiyee !!"
        
if __name__=="__main__":
    main()
        
        
                    
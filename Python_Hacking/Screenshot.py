from PIL import ImageGrab
import os

def screenshot():
    try:
        im = ImageGrab.grab()
        os.mkdir('C:\Windows_Files')
        im.save('C:\Windows_Files\screenshot.png')
    except Exception,e:
        return str(e)
        
if __name__=="__main__":
    screenshot()
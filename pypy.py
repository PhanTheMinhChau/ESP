import pyautogui
import subprocess as sub
from time import sleep
from threading import Thread
from datetime import datetime, timedelta
pyautogui.FAILSAFE = False
file = open("abc.hta", "wb")
a = """<hta:application id="oBVC" applicationname="BSOD" version="1.0" maximizebutton="no" minimizebutton="no" sysmenu="no" Caption="no" windowstate="maximize"/> <head><meta charset="utf-8"/></head><body bgcolor="#000088" scroll="no"> <font face="Lucida Console" size="4" color="#FFFFFF"> <p>Your PC ran into a problem and needs to restart. We're just collecting some error info, and we'll restart for you. If you'd like to know more, you can search online later for this error: SYSTEM_SERVICE_EXCEPTION </p><p>DGT36D6FG73FGF6FWBIW666WHJGFUEHF8V998</p><p>A problem has been detected and windows has been shutdown to prevent damage to your computer.</p> <p>If this is the first time you've seen this stop error screen, restart your computer, If this screen appears again, follow these steps:</p> <p>Check to make sure any new hardware or software is properly installed. If this is a new installation, ask your hardware or software manufacturer for any windows updates you might need.</p> <p>If problems continue, disable or remove anynewly installed hardware or software. Disable BIOS memory options such as caching or shadowing. If you need to use Safe Mode to remove or disable components, restart your computer, press F8 to select Advanced Startup Options, and then select Safe Mode.</p> <p>Technical information:</p> <p>*** gv3.sys - Address F86B5A89 base at F86B5000, DateStamp 3dd9919eb</p> <p>Beginning dump of physical memory</p> <p>Physical memory dump complete.</p> <p>Contact your system administrator or technical support group for further assistance.</p> <center><h1 style="font-size: 200px;color:red;">warning!!!</h1><center></font> </body></html>"""
file.write(a.encode('utf-8'))
file.close()
def abc():
    try:
        pyautogui.click(1600,700)
    except:
        pass
    pyautogui.click(1600,700)
def func1():
        sub.run('abc.hta', shell=True)
def func2():
    st = datetime.today() + timedelta(seconds = 120)
    while st > datetime.today():
        abc()
def func3():
    pyautogui.keyDown('ctrl')
    sleep(120)
    pyautogui.keyUp ('ctrl')
Thread(target = func1).start()
Thread(target = func2).start()
Thread(target = func3).start()
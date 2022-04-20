#hey you im here
#im just a noob in programming :)
import time
import os

os.system("apt install curl")
os.system("clear")
banner = """
              [+]Ip Tracker[+]
     ___________________________________
    |Author : Mika259                   |
    |Github : https://github.com/Mika259|
    +-----------------------------------+
"""

prs = """
want to see process :
[y]yes         [n]no
"""
os.system("clear")
print(banner)
print("Let's track ip address")
print(prs)
time.sleep(0.5)
ch = input("choose :")
chs = """
*used command [curl https://ipapi.co/<your ip here>/json']
 you can type this and see result without this tool.
"""
if ch == 'y':
    time.sleep(0.5)
    os.system("clear")
    print(banner)
    print("Let's track ip address")
    print(chs)
elif ch == 'n':
    time.sleep(0.5)
    print("ok")
    time.sleep(1)
    os.system("clear")
    print(banner)
    print("Let's track ip address")
else:
    print("error command , i think you dont want to see it.")
ip = input(str("[+]Enter ip :"))
time.sleep(1)
print("Get result :")

os.system("curl https://ipapi.co/"+ip+"/json")


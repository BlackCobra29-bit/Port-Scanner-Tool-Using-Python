import socket
import re
from tqdm import tqdm
import time
from colorama import Fore, Style
import platform
import os
import subprocess

if platform.system() == 'Windows':
    os.system('cls')
if platform.system() == 'Linux':
    subprocess.run('clear')

ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535

open_ports = []


def Print_Logo():
    Colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[39m']
    print('\t')
    Logo = r''' ██▓███   ▒█████   ██▀███  ▄▄▄█████▓     ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒   ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░      ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░    ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░      ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░       ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░░       ░ ░ ░ ▒    ░░   ░   ░         ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ V 1.0
             ░ ░     ░                       ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
                                                ░                                                                                                                       
                                                                         
                                                                    '''

    for Line in Logo.split('\n'):
        time.sleep(0.2)
        print(Fore.RED + Line)

Print_Logo()
print(Fore.LIGHTGREEN_EX)

print('\t\tAuthor: Tesfahiwet Truneh')
time.sleep(0.2)
print('\t\tGithub: https://github.com/deamatsoftware')
time.sleep(0.2)
print('\t\tEmail: \teminemmerne@gmail.com\n' + Style.RESET_ALL)
time.sleep(0.2)

while True:
    ip_add_entered = input("\n" + Fore.LIGHTBLUE_EX + "[*]" + Style.RESET_ALL + " Please enter the ip address that you want to scan: ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid ip address")
        break
    else:
        print('please enter valid ip address')

while True:

    print("Please enter the range of ports (ex 60-120)")
    port_range = input("Enter port range: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

for i in tqdm(range(port_max-port_min+1), desc= Fore.LIGHTGREEN_EX + "Scanning " + str(port_max-port_min) + " Ports ", ncols=75):
    time.sleep(0.0000000001)

for port in range(port_min, port_max + 1):

    try:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.settimeout(0.5)

            s.connect((ip_add_entered, port))

            print(Fore.LIGHTYELLOW_EX + "[+]" + " Open Port Found at " + str(port) + Style.RESET_ALL)

            open_ports.append(port)
            time.sleep(0.0000001)

    except:
        print(Fore.LIGHTBLUE_EX + "[+]" + Style.RESET_ALL + " Port " + str(port) + ' Closed port ' + Style.RESET_ALL)
        pass

for port in open_ports:
    print(f"Port {port} is open on {ip_add_entered}.")
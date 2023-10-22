import requests
from colorama import Fore, Style
import argparse

def main(url, wordlist_path):
    print(Fore.GREEN + "~~~~~FUZZER~~~~~" + Style.RESET_ALL)

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple fuzzer to find resources on a web server.")
    parser.add_argument('-url', required=True, help="The target URL with the placeholder 'FUZZ'.")
    parser.add_argument('-wordlist', required=True, help="Path to the wordlist file.")
    args = parser.parse_args()

    if args.url and args.wordlist:
        main(args.url, args.wordlist)

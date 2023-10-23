import os
import requests
from colorama import Fore, Style
import argparse
import time

RATE_LIMIT = 5 # requests per second

def main(url, wordlist_dir):
    print(Fore.GREEN + "~~~~~FUZZER~~~~~" + Style.RESET_ALL)

    # Check if the wordlist directory exists
    if not os.path.exists(wordlist_dir):
        print(Fore.RED + f"[-] Wordlist directory '{wordlist_dir}' does not exist." + Style.RESET_ALL)
        return

    # Get a list of all wordlist files in the directory
    wordlist_files = [f for f in os.listdir(wordlist_dir) if os.path.isfile(os.path.join(wordlist_dir, f))]

    if not wordlist_files:
        print(Fore.RED + f"[-] No wordlist files found in '{wordlist_dir}'." + Style.RESET_ALL)
        return

    print(Fore.YELLOW + f"[-] Starting scan with {len(wordlist_files)} wordlist files...\n" + Style.RESET_ALL)

    for wordlist_file in wordlist_files:
        with open(os.path.join(wordlist_dir, wordlist_file), 'r') as f:
            wordlist = [word.strip() for word in f.readlines()]

        for word in wordlist:
            new_url = url.replace("FUZZ", word)

            try:
                response = requests.get(new_url)
                if response.status_code == 200:
                    print(Fore.GREEN + f"[+] Found: {new_url}" + Style.RESET_ALL)
                else:
                    # print(Fore.RED + f"[-] Not Found: {new_url}" + Style.RESET_ALL)
                    pass
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"[-] Error: {e}" + Style.RESET_ALL)

        time.sleep(1/RATE_LIMIT)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple fuzzer to find resources on a web server.")
    parser.add_argument('-url', required=True, help="The target URL with the placeholder 'FUZZ'.")
    parser.add_argument('-wordlist-dir', required=True, help="Path to the directory containing wordlist files.")
    args = parser.parse_args()

    if args.url and args.wordlist_dir:
        main(args.url, args.wordlist_dir)

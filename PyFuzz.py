import os
import requests
from colorama import Fore, Style
import argparse
import time

RATE_LIMIT = 5 # requests per second

def main(url, wordlist_dir, timeout, max_retries):
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

    retries = 0

    for wordlist_file in wordlist_files:
        with open(os.path.join(wordlist_dir, wordlist_file), 'r', encoding="utf-8") as f:
            wordlist = [word.strip() for word in f.readlines()]

        for word in wordlist:
            new_url = url.replace("FUZZ", word)

            backoff_time = 1  # initial backoff time in seconds

            while retries < max_retries:
                try:
                    response = requests.get(new_url, timeout=timeout)
                    if response.status_code == 200:
                        print(Fore.GREEN + f"[+] Found: {new_url}" + Style.RESET_ALL)
                    break  # exit the retry loop if request was successful
                # catch timeouts
                except requests.exceptions.Timeout:
                    print (Fore.RED + f"[-] Timeout: {new_url}" + Style.RESET_ALL)
                    retries += 1
                    if retries < max_retries:
                        print(Fore.YELLOW + f"[-] Retrying in {backoff_time} seconds...\n" + Style.RESET_ALL)
                        time.sleep(backoff_time)
                        backoff_time *= 2
                    else:
                        print(Fore.RED + "[-] Max retries reached. Exiting..." + Style.RESET_ALL)
                # catch connection errors
                except requests.exceptions.ConnectionError:
                    print(Fore.RED + f"[-] Error: Unable to connect to {new_url}" + Style.RESET_ALL)
                    retries += 1
                    if retries < max_retries:
                        print(Fore.YELLOW + f"[-] Retrying in {backoff_time} seconds...\n" + Style.RESET_ALL)
                        time.sleep(backoff_time)
                        backoff_time *= 2
                    else:
                        print(Fore.RED + "[-] Max retries reached. Exiting..." + Style.RESET_ALL)
                # catch all other exceptions
                except requests.exceptions.RequestException as e:
                    print(Fore.RED + f"[-] Error: {e}" + Style.RESET_ALL)
                    retries += 1
                    if retries < max_retries:
                        print(Fore.YELLOW + f"[-] Retrying in {backoff_time} seconds...\n" + Style.RESET_ALL)
                        time.sleep(backoff_time)
                        backoff_time *= 2  # double the backoff time
                    else:
                        print(Fore.RED + "\n[-] Max retries reached. Exiting..." + Style.RESET_ALL)

        time.sleep(1/RATE_LIMIT)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple fuzzer to find resources on a web server.")
    parser.add_argument('-url', required=True, help="The target URL with the placeholder 'FUZZ'.")
    parser.add_argument('-wordlist-dir', required=True, help="Path to the directory containing wordlist files.")
    parser.add_argument('-timeout', type=int, default=10, help="Timeout for requests in seconds.")
    parser.add_argument('-max-retries', type=int, default=5, help="Maximum number of retries in case of network issues.")
    args = parser.parse_args()

    if args.url and args.wordlist_dir:
        main(args.url, args.wordlist_dir, args.timeout, args.max_retries)

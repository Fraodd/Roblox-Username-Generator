import requests
from colorama import Fore, init
from random import choices, choice
import time

init(autoreset=True)

# List of colors for terminal output
colors = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
]

def check(username_length):
    while True:
        # Generate a random username based on the user-specified length
        username = ''.join(choices('abcdefghijklmnopqrstuvwxyz1234567890', k=username_length))
        col = choice(colors)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }

        # URL to check profile existence
        url = f'https://www.roblox.com/users/profile?username={username}'

        try:
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                # Profile exists, username is taken
                print(f"{Fore.RED}[-] {username} Taken")
            elif response.status_code == 404:
                # Profile not found, username is available
                print(f"{Fore.GREEN}[+] {username} Available")
            else:
                print(f"{Fore.BLUE}[!] Unexpected Status Code: {response.status_code}")
                
        except requests.exceptions.HTTPError as http_err:
            print(f"{Fore.RED}[!] HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            print(f"{Fore.RED}[!] Connection error occurred: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            print(f"{Fore.RED}[!] Timeout error occurred: {timeout_err}")
        except requests.RequestException as req_err:
            print(f"{Fore.RED}[!] An error occurred: {req_err}")

        # Shortened sleep to 1 second for faster iteration
        time.sleep(0)

def main_menu():
    print(Fore.CYAN + "\n--- Roblox Username Checker ---\n")
    print("1. Start checking usernames")
    print("2. Exit\n")

    while True:
        choice = input(Fore.CYAN + "Enter your choice (1 or 2): ")

        if choice == '1':
            while True:
                try:
                    username_length = int(input(Fore.CYAN + "Enter the number of characters for the usernames (2-20): "))
                    if 2 <= username_length <= 20:
                        print(Fore.CYAN + f"\n[!] Starting to check usernames with {username_length} characters...\n")
                        check(username_length)
                    else:
                        print(Fore.RED + "[!] Please enter a number between 2 and 20.")
                except ValueError:
                    print(Fore.RED + "[!] Invalid input. Please enter a number.")
        elif choice == '2':
            print(Fore.CYAN + "\n[!] Exiting the program. Goodbye!")
            break
        else:
            print(Fore.RED + "[!] Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print(Fore.CYAN + "\n[!] Program stopped by user.")

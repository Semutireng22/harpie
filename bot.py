import json
import time
import random
import requests
from colorama import Fore, Style, init
from datetime import timedelta

# Inisialisasi colorama
init(autoreset=True)

# Fake User-Agents
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'
]

def get_random_user_agent():
    return random.choice(user_agents)

def random_delay(min_delay=1, max_delay=5):
    delay = random.randint(min_delay, max_delay)
    time.sleep(delay)

def perform_scan(address):
    print(f"{Fore.YELLOW}Scanning address {address}...", end="\r")
    random_delay()

    url = f"https://harpie.io/api/addresses/{address}/queue-health/"
    payload = {
        "chainId": 1,
        "manualScan": True
    }

    try:
        headers = {
            'User-Agent': get_random_user_agent(),
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://harpie.io/',
            'Origin': 'https://harpie.io',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache'
        }
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        # Ekstrak data penting dari respons
        stats = response.json().get("stats", {})
        percent_immune = stats.get("percentImmune", "N/A")
        percent_verified = stats.get("percentVerified", "N/A")
        activity_score = stats.get("activityScore", "N/A")

        print(f"{Fore.GREEN}✅ Scan successful for address {address}")
        if percent_immune != "N/A":
            print(f"{Fore.CYAN}📊 Percent Immune: {percent_immune}%")
        if percent_verified != "N/A":
            print(f"{Fore.CYAN}✅ Percent Verified: {percent_verified}%")
        if activity_score != "N/A":
            print(f"{Fore.CYAN}📈 Activity Score: {activity_score}")

        alerts = response.json().get("alerts", "{}")
        if alerts and alerts != "{}":
            print(f"{Fore.YELLOW}⚠️ Alerts: {alerts}")
        else:
            print(f"{Fore.GREEN}✅ No alerts detected.")

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}❌ Error scanning address {address}: {e}")

def read_addresses_from_file():
    try:
        with open('addresses.json', 'r') as file:
            addresses = json.load(file)
            return addresses if isinstance(addresses, list) else []
    except FileNotFoundError:
        return []

def save_addresses_to_file(addresses):
    with open('addresses.json', 'w') as file:
        json.dump(addresses, file, indent=2)

def add_address(addresses):
    new_address = input(f"{Fore.YELLOW}👉 Please enter the Ethereum address to add: ")
    if not new_address.startswith("0x") or len(new_address) != 42:
        print(f"{Fore.RED}❌ Invalid Ethereum address format. Please provide a valid address.")
        return addresses

    if new_address in addresses:
        print(f"{Fore.YELLOW}⚠️ Address {new_address} already exists in the list.")
    else:
        addresses.append(new_address)
        print(f"{Fore.GREEN}✅ Address {new_address} added successfully.")

    return addresses

def start_scanner(addresses):
    interval = 24 * 60 * 60  # 24 jam dalam detik
    print(f"{Fore.YELLOW}\n🚀 Starting scanner for {len(addresses)} address(es)...")

    def scan_all_addresses():
        for address in addresses:
            perform_scan(address)
            random_delay(2, 10)

    scan_all_addresses()

    while True:
        countdown = interval
        print(f"{Fore.YELLOW}\n⏰ Next scan will run in:")
        while countdown > 0:
            hours, remainder = divmod(countdown, 3600)
            minutes, seconds = divmod(remainder, 60)
            print(f"{Fore.CYAN}⏳ {hours}h {minutes}m {seconds}s", end="\r")
            time.sleep(1)
            countdown -= 1

        print(f"{Fore.GREEN}\n\n⏰ Running scheduled scan for all addresses...")
        scan_all_addresses()

print(f"""{Style.BRIGHT}{Fore.BLUE}
===========================================
=           HARPIE AUTO SCANNER           =
===========================================
=       Channel : t.me/ugdairdrop         =
===========================================
""")

addresses = read_addresses_from_file()

if not addresses:
    print(f"{Fore.YELLOW}ℹ️ No addresses found. Please add at least one address to begin.")
    addresses = add_address(addresses)
    save_addresses_to_file(addresses)
else:
    print(f"{Fore.GREEN}✅ Loaded {len(addresses)} address(es) from file:")
    for idx, addr in enumerate(addresses, start=1):
        print(f"{Fore.CYAN}{idx}. {addr}")

while True:
    print(f"""{Style.BRIGHT}{Fore.BLUE}
===========================================
=               Main Menu                 =
===========================================
1. Add new address
2. Start scanning
3. Exit
""")

    choice = input(f"{Fore.YELLOW}👉 Enter your choice: ")

    if choice == "1":
        addresses = add_address(addresses)
        save_addresses_to_file(addresses)
    elif choice == "2":
        if not addresses:
            print(f"{Fore.RED}❌ No addresses available to scan. Please add an address first.")
        else:
            start_scanner(addresses)
            print(f"{Fore.GREEN}✅ Scanner started successfully! Awaiting next execution...")
            break
    elif choice == "3":
        print(f"{Fore.GREEN}👋 Exiting the program. Goodbye!")
        break
    else:
        print(f"{Fore.RED}❌ Invalid choice. Please select a valid option.")

import requests
import time

ETHERSCAN_API_KEY = "your_etherscan_api_key"
WALLET_ADDRESS = "0xYourWalletAddress"

def get_balance(address):
    """
    Fetch the current ETH balance of the given wallet address using Etherscan API.
    """
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url).json()
    balance_wei = int(response["result"])
    balance_eth = balance_wei / 10**18
    return balance_eth

def monitor():
    """
    Monitor wallet balance changes every 60 seconds and print alert when change is detected.
    """
    prev_balance = get_balance(WALLET_ADDRESS)
    print(f"Initial balance: {prev_balance} ETH")
    while True:
        time.sleep(60)
        current_balance = get_balance(WALLET_ADDRESS)
        if current_balance != prev_balance:
            print(f"Balance changed! New balance: {current_balance} ETH")
            # Add notification logic here (e.g., Telegram, Discord)
            prev_balance = current_balance

if __name__ == "__main__":
    monitor()

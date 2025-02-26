# // First Install Python Libraries //
# // pip install requests colorthon cryptofuzz requests-random-user-agent//
# // Import Libraries //
import random, requests, time, os, sys
import requests_random_user_agent
from cryptofuzz import Ethereum, Dogecoin, Convertor
from colorthon import Colors


# // terminal title changed all os
def titler(text_title: str):
    sys.stdout.write(f"\x1b]2;{text_title}\x07")
    sys.stdout.flush()


# // terminal clear logs
def clearNow(): os.system("cls") if 'win' in sys.platform.lower() else os.system("clear")


# // ethereum rate //
def eth_rate(eth: float) -> int:
    url = "https://ethbook.guarda.co/api/v2/tickers/?currency=usd"
    req = requests.get(url)
    res = req.json()
    if req.status_code == 200:
        return int(eth * res.get("rates").get("usd"))
    else:
        return 0


# // dogecoin rate //
def doge_rate(doge: float) -> int:
    url = "https://dogecoin.atomicwallet.io/api/v2/tickers/?currency=usd"
    req = requests.get(url)
    res = req.json()
    if req.status_code == 200:
        return int(doge * res.get("rates").get("usd"))
    else:
        return 0


# // bnb rate //
def bnb_rate(bnb: float) -> int:
    url = "https://bsc-nn.atomicwallet.io/api/v2/tickers/?currency=usd"
    req = requests.get(url)
    res = req.json()
    if req.status_code == 200:
        return int(bnb * res.get("rates").get("usd"))
    else:
        return 0


# // Delay Printer //
def printer(text: str):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)


# // terminal clear
clearNow()

# // Colors //
red = Colors.RED
green = Colors.GREEN
cyan = Colors.CYAN
yellow = Colors.YELLOW
reset = Colors.RESET
# // check bip39 file in directory //
if os.path.exists("bip39.txt"):
    bip = True
else:
    # // if False Download bip39.txt from URL,
    bip = False

if not bip:
    # // bip39 phrase file //
    bip39_url = "https://raw.githubusercontent.com/Pymmdrza/Dumper-Mnemonic/mainx/bip39.txt"
    # // bip39 file download //
    printer(f"{yellow}Downloading bip39 file...{reset}\n")
    titler("Downloading bip39 file...")
    reqBip = requests.get(bip39_url)
    content_bip = reqBip.content.decode("utf-8")
    # // bip39 file write //
    with open("bip39.txt", "w", encoding="utf-8") as filebip:
        filebip.write(content_bip)
    titler("Download bip39.txt Complete.")
    printer(f"{green}Downloaded bip39 file Successfully.{reset}\n\n")

clearNow()


# // Checker Ethereum Balance From Atomic Wallet //
def CheckBalanceEthereum(address: str) -> str:
    url = f"https://ethbook.guarda.co/api/v2/address/{address}"
    req = requests.get(url)
    if req.status_code == 200:
        bal = req.json()["balance"]
        return str(bal)
    else:
        return "0"


# // Checker Dogecoin Balance From Atomic Wallet //
def CheckBalanceDogecoin(address: str) -> str:
    url = f"https://dogecoin.atomicwallet.io/api/v2/address/{address}"
    req = requests.get(url)
    if req.status_code == 200:
        bal = req.json()["balance"]
        return str(bal)
    else:
        return "0"


# // Checker BNB Balance From Atomic Wallet //
def CheckBalanceBNB(address: str) -> str:
    url = f"https://bsc-nn.atomicwallet.io/api/v2/address/{address}"
    req = requests.get(url)
    if req.status_code == 200:
        bal = req.json()["balance"]
        return str(bal)
    else:
        return "0"


# // Variables //
eth = Ethereum()
doge = Dogecoin()
util = Convertor()

# // Counter //
z = 0
ff = 0
found = 0
usd = 0

# // bip39 file read //
file_bip = "bip39.txt"
b_read = open(file_bip, "r")
bip39 = b_read.read()
b_read.close()

# // bip39 words split to list //
words = bip39.split("\n")
while True:
    # // Counter Total Generated and Converted Mnemonic //
    z += 1
    # // Counter detail to title //
    titler(f"Gen: {z} / Con: {ff} / USD: {usd} $")
    # // Size choice for mnemonic //
    rand_num = random.choice([12, 24])
    # // Random Mnemonic Generator //
    mnemonic = " ".join(random.choice(words) for _ in range(rand_num))
    # // Convert Mnemonic to Hex from Cryptofuzz//
    convert_hex = util.mne_to_hex(mnemonic)
    # // Generated Ethereum Address From Private Key Hex //
    eth_addr = eth.hex_addr(convert_hex)
    # // Generated Dogecoin Address From Private Key Hex //
    doge_addr = doge.hex_addr(convert_hex)
    # // Check Balance for Ethereum, Dogecoin, BNB //
    eth_bal = CheckBalanceEthereum(eth_addr)
    bnb_bal = CheckBalanceBNB(eth_addr)
    doge_bal = CheckBalanceDogecoin(doge_addr)
    # // Convert Balance to Decimal //
    eth_balance = int(eth_bal) / 1000000000000000000
    doge_balance = int(doge_bal) / 100000000
    bnb_balance = int(bnb_bal) / 1000000000000000000
    # // Check Ethereum Address if Balance is greater than 0 //
    # // Saved Details in found.txt on current directory //
    if eth_balance > 0:
        ff += 1
        found += eth_balance
        # // Append Rate Data in Title Terminal for Total USD Found
        usd += eth_rate(eth_balance)
        titler(f"Gen: {z} / Con: {ff} / USD: {usd} $")
        with open("found.txt", "a") as dr:
            dr.write(f"ETH: {eth_addr} | Balance: {eth_balance}\n"
                     f"Mnemonic: {mnemonic}\n"
                     f"Private Key: {convert_hex}\n")
    # // Check Dogecoin Address if Balance is greater than 0
    # // Saved Details in found.txt on current directory
    if doge_balance > 0:
        ff += 1
        found += doge_balance
        # // Append Rate Data in Title Terminal for Total USD Found
        usd += doge_rate(doge_balance)
        titler(f"Gen: {z} / Con: {ff} / USD: {usd} $")
        with open("found.txt", "a") as dr:
            dr.write(f"DOGE: {doge_addr} | Balance: {doge_balance}\n"
                     f"Mnemonic: {mnemonic}\n"
                     f"Private Key: {convert_hex}\n")
    # // Check BNB Address if Balance is greater than 0
    # // Saved Details in found.txt on current directory
    if bnb_balance > 0:
        ff += 1
        found += bnb_balance
        # // Append Rate Data in Title Terminal for Total USD Found
        usd += bnb_rate(bnb_balance)
        titler(f"Gen: {z} / Con: {ff} / USD: {usd} $")
        with open("found.txt", "a") as dr:
            dr.write(f"BNB: {eth_addr} | Balance: {bnb_balance}\n"
                     f"Mnemonic: {mnemonic}\n"
                     f"Private Key: {convert_hex}\n")

    else:
        # // Space Mode for Output Logs
        s = " "
        sp = s * 16
        spc_eth = sp + s * (43 - len(eth_addr))
        spc_doge = sp + s * (43 - len(doge_addr))
        # // Print Output Logs with Pretty Type Format
        print(f"[{z} | Found:{ff}]  ETH: {cyan}{eth_addr}{reset}{spc_eth}[Balance: {cyan}{eth_balance}{reset}]")
        print(f"[{z} | Found:{ff}]  BNB: {green}{eth_addr}{reset}{spc_eth}[Balance: {green}{bnb_balance}{reset}]")
        print(f"[{z} | Found:{ff}] DOGE: {yellow}{doge_addr}{reset}{spc_doge}[Balance: {yellow}{doge_balance}{reset}]")
        print(f"[{z} | Found:{ff}]  Mne: {red}{mnemonic[0:64]}{reset}")
        print(f"[{z} | Found:{ff}]  Hex: {convert_hex}")
        print(f"{'-' * 66}")

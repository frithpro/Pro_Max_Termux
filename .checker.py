import requests
from colorama import init, Fore, Back, Style

init(autoreset=True)
bin_number = input('𝕀𝕟𝕘𝕣𝕖𝕤𝕖 𝕖𝕝 𝕟ú𝕞𝕖𝕣𝕠 𝕕𝕖𝕝 𝔹𝕀ℕ: ')
url = f'https://lookup.binlist.net/{bin_number}'

response = requests.get(url)

if response.status_code == 200:
    bin_info = response.json()
    print("")
    print(Fore.RED +"𝕀ℕ𝔽𝕆ℝ𝕄𝔸ℂ𝕀𝕆ℕ 𝔻𝔼𝕃 𝔹𝕀ℕ" + Fore.RESET) 
    print("")
    print(f'𝑁ú𝑚𝑒𝑟𝑜 𝑑𝑒 𝑡𝑎𝑟𝑗𝑒𝑡𝑎: {Fore.GREEN}{bin_number}{Fore.RESET}')
    print(f'𝑀𝑎𝑟𝑐𝑎 𝑑𝑒 𝑡𝑎𝑟𝑗𝑒𝑡𝑎: {Fore.GREEN}{bin_info.get("brand", "No disponible")}{Fore.RESET}')
    print(f'𝑇𝑖𝑝𝑜 𝑑𝑒 𝑡𝑎𝑟𝑗𝑒𝑡𝑎: {Fore.GREEN}{bin_info.get("type", "No disponible")}{Fore.RESET}')
    print(f'𝑆𝑐ℎ𝑒𝑚𝑒/𝑁𝑒𝑡𝑤𝑜𝑟𝑘: {Fore.GREEN}{bin_info.get("scheme", "No disponible")}{Fore.RESET}')
    print(f'𝐿𝑎𝑟𝑔𝑜 𝑑𝑒 𝑙𝑎 𝑡𝑎𝑟𝑗𝑒𝑡𝑎: {Fore.GREEN}{bin_info.get("number_length", "16")}{Fore.RESET}')
    print(f'𝐴𝑙𝑔𝑜𝑟𝑖𝑡𝑚𝑜 𝑑𝑒 𝐿𝑢ℎ𝑛: {Fore.GREEN}{bin_info.get("luhn", "Yes")}{Fore.RESET}')
    print(f'𝑃𝑎í𝑠 𝑒𝑚𝑖𝑠𝑜𝑟: {Fore.GREEN}{bin_info["country"].get("name", "No disponible")}{Fore.RESET}')
    print(f'𝐶ó𝑑𝑖𝑔𝑜 𝑑𝑒 𝑝𝑎í𝑠 𝑒𝑚𝑖𝑠𝑜𝑟: {Fore.GREEN}{bin_info["country"].get("alpha2", "No disponible")}{Fore.RESET}')
    print(f'𝑁𝑜𝑚𝑏𝑟𝑒 𝑑𝑒𝑙 𝑏𝑎𝑛𝑐𝑜 𝑒𝑚𝑖𝑠𝑜𝑟: {Fore.GREEN}{bin_info["bank"].get("name", "No disponible")}{Fore.RESET}')
    print(f'𝑆𝑖𝑡𝑖𝑜 𝑤𝑒𝑏 𝑑𝑒𝑙 𝑏𝑎𝑛𝑐𝑜 𝑒𝑚𝑖𝑠𝑜𝑟: {Fore.GREEN}{bin_info["bank"].get("url", "No disponible")}{Fore.RESET}')
    print(f'𝑇𝑒𝑙é𝑓𝑜𝑛𝑜 𝑑𝑒𝑙 𝑏𝑎𝑛𝑐𝑜 𝑒𝑚𝑖𝑠𝑜𝑟: {Fore.GREEN}{bin_info["bank"].get("phone","No disponible")}{Fore.RESET}')
    print("")
else:
    print(f'𝔼𝕝 𝔹𝕀ℕ {bin_number} 𝕟𝕠 𝕖𝕤 𝕧á𝕝𝕚𝕕𝕠 𝕠 𝕟𝕠 𝕤𝕖 𝕖𝕟𝕔𝕠𝕟𝕥𝕣𝕒𝕣𝕠𝕟 𝕣𝕖𝕤𝕦𝕝𝕥𝕒𝕕𝕠𝕤.') 

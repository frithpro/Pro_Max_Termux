import random
import json
from colorama import Fore, Style

def card_luhn_checksum_is_valid(card_number):
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(num_digits):
        digit = int(card_number[count])
        if not (( count & 1 ) ^ oddeven ):
            digit *= 2
        if digit > 9:
            digit -= 9
        sum += digit

    return (sum % 10) == 0

def generate_card_number(card_type):
    card_number = ""

    if card_type == "𝕧𝕚𝕤𝕒":
        card_number = "4"
    elif card_type == "𝕞𝕒𝕤𝕥𝕖𝕣𝕔𝕒𝕣𝕕":
        card_number = "5" + str(random.randint(1, 5))
    elif card_type == "𝕒𝕞𝕖𝕩":
        card_number = "3" + str(random.choice([4, 7]))
    elif card_type == "𝕕𝕚𝕤𝕔𝕠𝕧𝕖𝕣":
        card_number = "6" + "0" + "1" + "1"
    elif card_type == "𝕕𝕚𝕟𝕖𝕣𝕤":
        card_number = "3" + "0" + str(random.choice([0, 6, 8])) + str(random.randint(0, 9))

    while len(card_number) < 15:
        card_number += str(random.randint(0, 9))

    digits = [int(x) for x in card_number]
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    checksum = sum(digits) * 9 % 10
    card_number += str(checksum)

    if not card_luhn_checksum_is_valid(card_number):
        card_number = generate_card_number(card_type)

    return card_number

def generate_expiry_date():
    month = random.randint(1, 12)
    year = random.randint(2024, 2029)
    return f"{month:02}/{year:02}"

def generate_cvv():
    return str(random.randint(100, 999))

card_type = input("𝔼𝕤𝕔𝕠𝕘𝕖𝕣 𝕥𝕚𝕡𝕠 𝕕𝕖 𝕥𝕒𝕣𝕛𝕖𝕥𝕒 (𝕧𝕚𝕤𝕒, 𝕞𝕒𝕤𝕥𝕖𝕣𝕔𝕒𝕣𝕕, 𝕒𝕞𝕖𝕩, 𝕕𝕚𝕤𝕔𝕠𝕧𝕖𝕣 𝕠 𝕕𝕚𝕟𝕖𝕣𝕤): ")
num_cards = int(input("𝔼𝕤𝕔𝕠𝕘𝕖𝕣 𝕔𝕒𝕟𝕥𝕚𝕕𝕒𝕕 𝕒 𝕘𝕖𝕟𝕖𝕣𝕒𝕣: "))

card_details = []
for i in range(num_cards):
    card_number = generate_card_number(card_type)
    expiry_date = generate_expiry_date()
    cvv = generate_cvv()

    card_info = {"numero_tarjeta": card_number, "fecha_vencimiento": expiry_date, "cvv": cvv, "tipo_tarjeta": card_type.capitalize()}
    card_details.append(card_info)

result = {"tarjetas_generadas": card_details}
json_result = json.dumps(result, indent=4)

print(f"\n𝕃𝕠𝕤 𝕟ú𝕞𝕖𝕣𝕠𝕤 𝕕𝕖 𝕥𝕒𝕣𝕛𝕖𝕥𝕒 𝕕𝕖 𝕔𝕣é𝕕𝕚𝕥𝕠 𝕘𝕖𝕟𝕖𝕣𝕒𝕕𝕠𝕤 𝕤𝕠𝕟:\n")

for card in card_details:
    cc_number = card["numero_tarjeta"]
    date = card["fecha_vencimiento"]
    cvv = card["cvv"]
    card_type = card["tipo_tarjeta"]
    print(f"𝑇𝑎𝑟𝑗𝑒𝑡𝑎 𝑑𝑒 𝑐𝑟𝑒𝑑𝑖𝑡𝑜: {Fore.GREEN}{cc_number}{Fore.RESET}")
    print(f"𝐹𝑒𝑐ℎ𝑎 𝑑𝑒 𝑒𝑥𝑝𝑖𝑟𝑎𝑐𝑖𝑜𝑛: {Fore.GREEN}{date}{Fore.RESET}")
    print(f"𝐶𝑜𝑑𝑖𝑔𝑜 𝑑𝑒 𝑠𝑒𝑔𝑢𝑟𝑖𝑑𝑎𝑑 𝐶𝑉𝑉: {Fore.RED}{cvv}{Fore.RESET}")
    print(f"𝑇𝑖𝑝𝑜 𝑑𝑒 𝑡𝑎𝑟𝑗𝑒𝑡𝑎: {Fore.YELLOW}{card_type}{Fore.RESET}\n")


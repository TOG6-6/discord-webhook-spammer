import discord_webhook
from discord_webhook import DiscordEmbed, DiscordWebhook
import string
import random
import time
import requests
import colorama
import json
from colorama import *

colorama.init()

def sbammah():
    webhook = input(Fore.YELLOW + "[>] Enter The Webhook Link: ")
    message = input(Fore.GREEN + "[>] Enter The Message: ")
    delay = float(input(Fore.RED + "[>] Enter The Delay (EX: 0.1): "))
    print(Fore.RESET + '')

    while True:

        print(Fore.CYAN + "Sending -> " + message)
        print(Fore.RESET + " ")
        try:
            time.sleep(delay)
            _data = requests.post(webhook, json={'content': message})

            if _data.status_code == 204:
                print(Fore.CYAN + "Sent -> " + message) 
        except:
            print("Something Happend! | Probably Broken Webhook -> " + webhook)
            time.sleep(5)
            exit()

x = 5
while x == 5:
    sbammah()
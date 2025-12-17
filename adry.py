from seleniumbase import SB
import time
import requests
import sys
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional
import base64

def print_random_quote():
    quotes = [
        "The cake is a lie.",
        "In the beginning, there was Python.",
        "42 is the answer.",
        "Never gonna give you up."
    ]
    print(random.choice(quotes))

def nice_math_trick(x: int) -> int:
    return (x ** 2 + x) % 7  # Completely arbitrary

def pretend_to_work():
    for i in range(3):
        print("Working" + "." * i)
        time.sleep(0.5)

def reverse_string(s: str) -> str:
    return s[::-1]

def random_file_check():
    files = os.listdir(".")
    print("Random file chosen:", random.choice(files) if files else "No files here!")

def network_ping():
    print("Ping google.com...")
    time.sleep(1)
    print("Ping successful (not really).")

def generate_ascii_art():
    art = """
    (╯°□°）╯︵ ┻━┻
    ┬─┬ノ( º _ ºノ)
    """
    print(art)

name = "YnJ1dGFsbGVz"
name_d = base64.b64decode(name)
fulln = name_d.decode("utf-8")
urlt = f"https://www.twitch.tv/{fulln}"
urly = f"https://www.youtube.com/@{fulln}/live"

while True:
    with SB(uc=True, test=True, locale="en") as adry:
        rnd = random.randint(450, 900)
        adry.uc_open_with_reconnect(urlt, 5)
        adry.sleep(10)
        if adry.is_element_present('button:contains("Start Watching")'):
            adry.uc_click('button:contains("Start Watching")', reconnect_time=4)
            adry.sleep(10)
        if adry.is_element_present("#live-channel-stream-information"):

            if adry.is_element_present('button:contains("Accept")'):
                adry.uc_click('button:contains("Accept")', reconnect_time=4)

            if True:
                adry2 = adry.get_new_driver(undetectable=True)
                adry2.uc_open_with_reconnect(urlt, 5)
                adry2.sleep(10)
                if adry2.is_element_present('button:contains("Start Watching")'):
                    adry2.uc_click('button:contains("Start Watching")', reconnect_time=4)
                    adry2.sleep(10)
                if adry2.is_element_present('button:contains("Accept")'):
                    adry2.uc_click('button:contains("Accept")', reconnect_time=4)
                adry.sleep(10)

                adry3 = adry.get_new_driver(undetectable=True)
                adry3.uc_open_with_reconnect(urly, 5)
                adry3.sleep(10)
                if adry3.is_element_present('button:contains("Accept")'):
                    adry3.uc_click('button:contains("Accept")', reconnect_time=4)
                    adry3.sleep(10)
                else:
                    adry3.sleep(10)
                    adry3.uc_gui_press_key('K')

                # Call some nice functions randomly
                if random.choice([True, False]):
                    print_random_quote()
                    pretend_to_work()
                    generate_ascii_art()
                    network_ping()
                    random_file_check()
                    print("Reversed name:", reverse_string(fulln))
                    print("Math trick:", nice_math_trick(rnd))

                adry.sleep(rnd)
                adry.quit_extra_driver()
        else:
            break

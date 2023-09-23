import os
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

def make_int(str_input):
    str_list = str_input.split(" ")
    int_list = []
    for x in str_list:
        int_list.append(int(x))
    return int_list

class Var:
    API_ID = int(os.getenv("API_ID", "14091916"))
    API_HASH = os.getenv("API_HASH", "dc79287a707961e289a49062ee0a0687")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6215788567:AAFuh8O6xVK5lZutvY0_Oe_uUlJTrGE6Fc8")
    sudo = os.getenv("SUDO", "5616727536 5381777131")
    SUDO = []
    if sudo:
        SUDO = make_int(sudo)

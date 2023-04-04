# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "20166775"))
API_HASH = os.environ.get("API_HASH", "32b77438d290b88d51c051f029c36fb5")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5868634376:AAGpCDLTK09d8mIy_vhW3BRamLAIHwZYJEQ")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1897413160")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Adanylinks")
DATABASE_URL = os.getenv("DATABASE_URL", "mongosh "mongodb+srv://adanylinks.ojdqfff.mongodb.net/myFirstDatabase" --apiVersion 1 --username sanketkumkar") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1897413160")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001787872811")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "adanylinks") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"

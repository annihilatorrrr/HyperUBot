from telethon import TelegramClient
from telethon.sessions import StringSession #not yet implemented!
from logging import basicConfig, DEBUG, getLogger

from sys import version_info #check python version

from dotenv import load_dotenv

from tg_userbot.config import ConfigClass #For now, config file only!

load_dotenv("config.env")

#For now, static
basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=DEBUG)

LOGS = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 6: #for now python 3.6
    LOGS.error("Required Python 3.6")
    quit(1)

#For now, config file only!
API_KEY = ConfigClass.API_KEY
API_HASH = ConfigClass.API_HASH

#add something for stringsession
bot = TelegramClient("tguserbot", API_KEY, API_HASH)
import telethon
from telethon.sync import TelegramClient as masterclient
from telethon import errors, functions, types, events , helpers
import asyncio
import aiohttp
import urllib.parse
from . import (
    Config, StreamTools, Streamer, Checkers
)
import io
import re
import os.path
import requests
from contextlib import redirect_stdout
from subprocess import PIPE, STDOUT, Popen
from telethon.tl.types import InputFile
from telethon.sessions import StringSession


class BareServer(Config, StreamTools, Streamer, Checkers):
    
    def __init__(self):
        
        self.client = telethon.TelegramClient(
            StringSession(), #self.config.SESS_NAME,
            self.config.APP_ID,
            self.config.API_HASH,
            
        ).start(bot_token=self.config.BOT_TOKEN)
        
        self.client2 = telethon.TelegramClient(
            StringSession(), #self.config.SESS_NAME2,
            self.config.APP_ID,
            self.config.API_HASH,
            
        ).start(bot_token=self.config.BOT_TOKEN2)
        
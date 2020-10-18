import telethon
from telethon.sync import TelegramClient as masterclient
from telethon import errors, functions, types, events , helpers
import asyncio
import aiohttp
import urllib.parse
from . import (
    Config, StreamTools, Streamer, Checkers
)
from .db import Db
import io
import re
import requests
from contextlib import redirect_stdout
from subprocess import PIPE, STDOUT, Popen
from telethon.tl.types import InputFile

ERROR = "**Expression:**\n```{}```\n\n**{}**: {}".format
SUCCESS = '**Expression:**\n```{}```\n\n**Result**\n```{}```\u200e'.format
SUCCESS_BASH = '**Bash expression:**\n```{}```\n\n\
**Result**\n```{}```\n\n**Error**```{}```\u200e'.format


class BareServer(Config, StreamTools, Streamer, Checkers , Db):
    client: telethon.TelegramClient
    
    def __init__(self, loop: asyncio.AbstractEventLoop):
        
        self.client = telethon.TelegramClient(
            self.config.SESS_NAME,
            self.config.APP_ID,
            self.config.API_HASH,
            loop=loop
        ).start(bot_token=self.config.BOT_TOKEN)
        
        self.client2 = telethon.TelegramClient(
            self.config.SESS_NAME2,
            self.config.APP_ID,
            self.config.API_HASH,
            loop=loop
        ).start(bot_token=self.config.BOT_TOKEN2)
        
        
        self.master = telethon.TelegramClient(
            "Sudo",
            self.config.APP_ID,
            self.config.API_HASH,
            loop=loop
        ).start()
        
        
       
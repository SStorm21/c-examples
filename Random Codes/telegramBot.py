import asyncio
import logging
import sys
import aiogram
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
token = '7120891229:AAG84SODjLR9sOa_887k8FBMTpvniRwLVis'

bot = Bot(token)
dp  = Dispatcher(Bot)

@dp.message_handler(Commands=['start'])
async def cmd_start(msg:type.Message):
    await msg.answer("hello!")
    
if __name__ == '__main__':
    executor.start_polling(dp)

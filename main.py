import os
import logging
import asyncio
from pyexpat.errors import messages

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.formatting import as_list

import Models
from Models import mortgage

load_dotenv()
MYTOKEN = os.getenv('token')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=MYTOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Welcome to FornoPizza telegram bot❗️\n"
                         "What kind of pizza would you like❓\n"
                         "/start - for starting and restarting \n"
                         "/property - Choose Pizza \n")

@dp.message(Command("property"))
async def property(message: types.Message):
    await message.answer("connect me to database")

dp.include_router(Models.router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
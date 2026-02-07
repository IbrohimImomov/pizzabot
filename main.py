import os
import logging
import asyncio

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile

import Models
from DataBase import DataBase

load_dotenv()
MYTOKEN = os.getenv('token')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=MYTOKEN)
dp = Dispatcher()

# Initialize database
db = DataBase("pizzabot.db")

# Static files directory
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")

@dp.message(Command("start"))
async def start(message: types.Message):
    # Add user to database
    db.add_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )
    await message.answer("Welcome to FornoPizza telegram bot❗️\n"
                         "What kind of pizza would you like❓\n"
                         "/start - for starting and restarting \n"
                         "/property - Choose Pizza \n")

@dp.message(Command("property"))
async def property(message: types.Message):
    # Get all pizzas from PizzaFactory
    pizzas = Models.PizzaFactory.get_all_pizzas()
    
    # Map pizza names to image files
    pizza_images = {
        "Papperoni": "Pizza_Papperoni.jpeg",
        "Barbecue": "Pizza_Barbecue.jpeg",
        "Sea Delights": "Pizza_SeaDelights.jpeg",
        "Alfredo": "Pizza_Alfredo.jpeg",
    }
    
    await message.answer("Here are our delicious pizzas! 🍕")
    
    for pizza in pizzas:
        # Build caption with pizza details
        caption = (
            f"🍕 <b>{pizza.name}</b>\n\n"
            f"💰 <b>Price:</b> {pizza.price:,.0f} UZS\n"
            f"🥖 <b>Dough:</b> {pizza.dough}\n"
            f"🍅 <b>Sauce:</b> {pizza.sauce}\n"
            f"🧀 <b>Toppings:</b> {', '.join(pizza.toppings)}"
        )
        
        filename = pizza_images.get(pizza.name)
        if filename:
            file_path = os.path.join(STATIC_DIR, filename)
            if os.path.exists(file_path):
                photo = FSInputFile(file_path)
                await message.answer_photo(photo, caption=caption, parse_mode="HTML")

dp.include_router(Models.router)

async def main():
    # Create database tables on startup
    await db.create_tables()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
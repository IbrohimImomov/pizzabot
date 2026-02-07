import asyncio
import time

from aiogram import Router, types, F
from aiogram.filters import Command


from aiogram.types import FSInputFile

router = Router()

@router.message(Command("models"))
async def mortgage(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    await message.answer("For interaction with the models"
                         "press the button", reply_markup=kb)

models_list = [
    ["Pizza_Papperoni"],
    ["Pizza_Barbecue"],
    ["Pizza_SeaDelights"],
    ["Pizza_Alfredo"],
]

models_path_files = [

    ("Pizza_Papperoni", "text about", "./static/Pizza_Papperoni.jpeg"),
    ("Pizza_Barbecue", "text about", "./static/Pizza_Barbecue.jpeg"),
    ("Pizza_SeaDelights", "text about", "./static/Pizza_SeaDelights.jpeg"),
    ("Pizza_Alfredo", "text about", "./static/Pizza_Alfredo.jpeg")
]



@router.message(F.text)
async def pizza_models(message: types.Message):
    if message.text == "super":
        data_for = []
        for name in models_path_files:
            data_for.append(0)
            await message.answer_photo(photo = FSInputFile(f"{name[2]}"), caption=f"Name: {name[1]}")
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        await message.answer("Select a pizza", reply_markup=kb.as_markup())
    elif message.text == "Pizza for all humans":
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        await message.answer("Select a pizza", reply_markup=kb.as_markup())
        photo = FSInputFile(f"{models_path_files[0]['path']}")
        await message.answer_photo(photo = photo, caption=models_path_files[0]["name"])
        await message.answer("Pizza_Papperoni")
    elif message.text == "Pizza for all humans":
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        await message.answer("Select a pizza", reply_markup=kb.as_markup())

@router.callback_query(F.data)
async def models_callback_query(callback_query: types.CallbackQuery):
    if callback_query.data == "Pizza_SeaDelilights":
        await callback_query.answer("Your order is being prepared ")
        await asyncio.sleep(3)
        await callback_query.message.answer("Your order has been handed over to the courier")
        await callback_query.message.answer()

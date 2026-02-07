from aiogram.utils.keyboard import (InlineKeyboardBuilder,
                                    ReplyKeyboardBuilder)

class Keyboards:
    def __init__(self, FornoPizza):
        self.PureStep = FornoPizza

    def inline_keyboard(self, data):
        self.inline_keyboard1 = InlineKeyboardBuilder
        for FornoPizza in data:
            self.inline_keyboard1.button(text=f"{FornoPizza[1]}", callback_data=FornoPizza[0])
        return self.inline_keyboard1

    def reply_keyboard(self, data):
        self.reply_keyboard1 = ReplyKeyboardBuilder
        for FornoPizza in data:
            self.inline_keyboard1.button(text=f"{FornoPizza}")
        return self.reply_keyboard1
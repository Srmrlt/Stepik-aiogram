from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (Message, KeyboardButton,
                           ReplyKeyboardMarkup, ReplyKeyboardRemove)


BOT_TOKEN: str = '6293522184:AAGp9WalX-8pBafVLYFYt6NFB0eQMN743nE'

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()

button_1: KeyboardButton = KeyboardButton(text='Кнопка 1')
button_2: KeyboardButton = KeyboardButton(text='Кнопка 2')
button_3: KeyboardButton = KeyboardButton(text='Кнопка 3')
button_4: KeyboardButton = KeyboardButton(text='Кнопка 4')
button_5: KeyboardButton = KeyboardButton(text='Кнопка 5')
button_6: KeyboardButton = KeyboardButton(text='Кнопка 6')
button_7: KeyboardButton = KeyboardButton(text='Кнопка 7')
button_8: KeyboardButton = KeyboardButton(text='Кнопка 8')
button_9: KeyboardButton = KeyboardButton(text='Кнопка 9')

my_keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[button_1, button_2, button_3],
              [button_4, button_5, button_6],
              [button_7, button_8, button_9]],
    resize_keyboard=True
)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Чего кошки боятся больше?',
                         reply_markup=my_keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)

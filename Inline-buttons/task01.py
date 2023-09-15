from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           Message)
from config_data.config import Config, load_config


config: Config = load_config()
bot: Bot = Bot(token=config.tg_bot.token,
               parse_mode='HTML')
dp: Dispatcher = Dispatcher()

url_btn_1: InlineKeyboardButton = InlineKeyboardButton(
    text='tra-ta-ta', url='https://stepik.org/120924')
url_btn_2: InlineKeyboardButton = InlineKeyboardButton(
    text='bot info', url='https://core.telegram.org/bots/api')

keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[url_btn_1], [url_btn_2]])


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='inline buttons with url',
                         reply_markup=keyboard)

if __name__ == '__main__':
    dp.run_polling(bot)

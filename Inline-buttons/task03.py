from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           Message, CallbackQuery)
from config_data.config import Config, load_config
from lexicon import LEXICON, BUTTONS
from create_inline_kb import create_inline_kb


config: Config = load_config()
bot: Bot = Bot(token=config.tg_bot.token,
               parse_mode='HTML')
dp: Dispatcher = Dispatcher()


@dp.message(CommandStart())
async def process_start_command(message: Message):
    keyboard = create_inline_kb(4, **BUTTONS)
    await message.answer(text='yeee',
                         reply_markup=keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           Message, CallbackQuery)
from config_data.config import Config, load_config


config: Config = load_config()
bot: Bot = Bot(token=config.tg_bot.token,
               parse_mode='HTML')
dp: Dispatcher = Dispatcher()

big_btn_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Big Button 1', callback_data='big_btn_1_pressed')
big_btn_2: InlineKeyboardButton = InlineKeyboardButton(
    text='Big Button 2', callback_data='big_btn_2_pressed')

keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[big_btn_1], [big_btn_2]])


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='inline buttons',
                         reply_markup=keyboard)


@dp.callback_query(Text(text=['big_btn_1_pressed']))
async def process_btn_1_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 1':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 1',
            reply_markup=callback.message.reply_markup)
    await callback.answer(text='Ура! Нажата кнопка 1',
                          show_alert=True)


@dp.callback_query(Text(text='big_btn_2_pressed'))
async def process_btn_2_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата БОЛЬШАЯ КНОПКА 2':
        await callback.message.edit_text(
            text='Была нажата БОЛЬШАЯ КНОПКА 2',
            reply_markup=callback.message.reply_markup)
    await callback.answer(text='Ура! Нажата кнопка 2')


if __name__ == '__main__':
    dp.run_polling(bot)

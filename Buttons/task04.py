from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo


BOT_TOKEN: str = '6293522184:AAGp9WalX-8pBafVLYFYt6NFB0eQMN743nE'

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()

kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

contact_btn: KeyboardButton = KeyboardButton(text='Send phone',
                                             request_contact=True)
geo_btn: KeyboardButton = KeyboardButton(text='Send location',
                                         request_location=True)
poll_btn: KeyboardButton = KeyboardButton(text='Create victorine',
                                          request_poll=KeyboardButtonPollType())
web_app_btn: KeyboardButton = KeyboardButton(text='Start web app',
                                             web_app=WebAppInfo(url='https://stepik.org/'))

kb_builder.row(contact_btn, geo_btn, poll_btn, web_app_btn, width=1)

keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True,
                                                     one_time_keyboard=True)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Экспериментируем со специальными кнопками',
                         reply_markup=keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)

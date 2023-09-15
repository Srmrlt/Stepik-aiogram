from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


BOT_TOKEN: str = '6293522184:AAGp9WalX-8pBafVLYFYt6NFB0eQMN743nE'

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()

kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

buttons: list[KeyboardButton] = [KeyboardButton(
    text=f'Кнопка {i + 1}') for i in range(10)]

kb_builder.row(*buttons, width=5)


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Чего кошки боятся больше?',
                         reply_markup=kb_builder.as_markup(resize_keyboard=True))


if __name__ == '__main__':
    dp.run_polling(bot)

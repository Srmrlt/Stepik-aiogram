from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


bot_api_token: str = '6293522184:AAGp9WalX-8pBafVLYFYt6NFB0eQMN743nE'

bot: Bot = Bot(token=bot_api_token)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    await message.answer("Hi!\nI'm echo-bot\nWrite me something")


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer("Write me, and I'll repeat it")


@dp.message()
async def send_echo(message: Message):
    try:
        print(message.json(indent=4, exclude_none=True))
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text='Not allowed type')


if __name__ == '__main__':
    dp.run_polling(bot)

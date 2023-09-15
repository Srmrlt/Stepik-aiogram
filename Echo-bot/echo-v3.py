from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ContentType


bot_api_token: str = '6293522184:AAGp9WalX-8pBafVLYFYt6NFB0eQMN743nE'

bot: Bot = Bot(token=bot_api_token)
dp: Dispatcher = Dispatcher()


async def process_start_command(message: Message):
    await message.answer("Hi!\nI'm echo-bot\nWrite me something")


async def process_help_command(message: Message):
    await message.answer("Write me, and I'll repeat it")


async def send_echo(message: Message):
    await message.reply(text=message.text)
    # await message.answer(text=message.text)


async def send_photo_echo(message: Message):
    print(message)
    await message.reply_photo(message.photo[2].file_id)


async def send_sticker_echo(message: Message):
    print(message)
    await message.reply_sticker(message.sticker.file_id)


dp.message.register(process_start_command, Command(commands=["start"]))
dp.message.register(process_help_command, Command(commands=["help"]))
dp.message.register(send_photo_echo, F.content_type == ContentType.PHOTO)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_echo)


if __name__ == '__main__':
    dp.run_polling(bot)

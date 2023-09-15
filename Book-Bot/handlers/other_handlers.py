from aiogram import Router
from aiogram.types import Message


router: Router = Router()


@router.message()
async def send_echo(message: Message):
    """
    send an echo to the user on any message
    """
    await message.answer(text=f'Это эхо! {message.text}')

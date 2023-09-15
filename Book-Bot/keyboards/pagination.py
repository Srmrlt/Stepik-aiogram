from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import BUTTONS_PG


def create_pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    """
    Function that generates a keyboard for a book page
    """
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    btn = [InlineKeyboardButton(
        text=BUTTONS_PG['RU'][button] if button in BUTTONS_PG else button,
        callback_data=button) for button in buttons]
    kb_builder.row(*btn)
    return kb_builder.as_markup()

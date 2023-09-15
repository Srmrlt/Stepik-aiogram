from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon import BUTTONS_BM
from services.file_handling import book


def create_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
    """
    Function that generates a bookmark keyboard
    """
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for mark in sorted(args):
        # Filling the keyboard with bookmark buttons in ascending order
        kb_builder.row(InlineKeyboardButton(
            text=f'{mark} - {book[mark][:100]}',
            callback_data=str(mark)))

    # Add two buttons "Edit" and "Cancel" to the keyboard at the end
    kb_builder.row(
        InlineKeyboardButton(
            text=BUTTONS_BM['RU']['edit_bookmarks_button'],
            callback_data='edit_bookmarks'),
        InlineKeyboardButton(
            text=BUTTONS_BM['RU']['cancel'],
            callback_data='cancel'),
        width=2)

    return kb_builder.as_markup()


def create_edit_keyboard(*args: int) -> InlineKeyboardMarkup:
    """
    Function that generates a keyboard for editing bookmarks
    """
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for mark in sorted(args):
        # Filling the keyboard with bookmark buttons in ascending order
        kb_builder.row(
            InlineKeyboardButton(
                text=f'{BUTTONS_BM["RU"]["del"]} {mark} - {book[mark][:100]}',
                callback_data=f'{mark}del'))

    # Add button "Cancel" to the keyboard at the end
    kb_builder.row(
        InlineKeyboardButton(
            text=BUTTONS_BM["RU"]["cancel"],
            callback_data='cancel'))

    return kb_builder.as_markup()

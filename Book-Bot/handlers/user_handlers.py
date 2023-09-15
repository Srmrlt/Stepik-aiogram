import copy

from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import InlineKeyboardMarkup

from lexicon.lexicon import START, HELP, NOTIFICATIONS
from filters.filters import IsDigitCallbackData, IsDelBookmarksCallbackData
from database.database import user_dict_template, users_db
from keyboards.pagination import create_pagination_keyboard
from keyboards.bookmarks_kb import (create_edit_keyboard,
                                    create_bookmarks_keyboard)
from services.file_handling import book


router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    """
    Processing the "/start" command;
    adding a user to the database;
    sending a welcome message
    """
    await message.answer(text=START['RU'])
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = copy.deepcopy(user_dict_template)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    """
    Processing the "/help" command;
    sending a message to the user with a list of available commands in the bot
    """
    await message.answer(text=HELP['RU'])


@router.message(Command(commands='beginning'))
async def process_beginning_command(message: Message):
    """
    Processing the "/beginning" command;
    sending the user the first page of the book with pagination buttons
    """
    users_db[message.from_user.id]['page'] = 1
    text = book[users_db[message.from_user.id]['page']]
    await message.answer(text=text,
                         reply_markup=_cr_pg_kb(message))


@router.message(Command(commands='continue'))
async def process_beginning_command(message: Message):
    """
    Processing the "/continue" command;
    sending the user the page of the book where the user stopped
    in the process of interacting with the bot
    """
    text = book[users_db[message.from_user.id]['page']]
    await message.answer(text=text,
                         reply_markup=_cr_pg_kb(message))


def _cr_pg_kb(m: Message | CallbackQuery) -> InlineKeyboardMarkup:
    """
    Creating a page switching keyboard (pagination keyboard)
    """
    return create_pagination_keyboard(
        'backward',
        f'{users_db[m.from_user.id]["page"]}/{len(book)}',
        'forward')


@router.message(Command(commands='bookmarks'))
async def process_bookmarks_command(message: Message):
    """
    Processing the "/bookmarks" command;
    sending the user a list of saved bookmarks, if any,
    or a message that there are no bookmarks
    """
    if users_db[message.from_user.id]["bookmarks"]:
        await message.answer(text=NOTIFICATIONS["RU"]["bookmarks"],
                             reply_markup=create_bookmarks_keyboard(
                                 *users_db[message.from_user.id]["bookmarks"]))
    else:
        await message.answer(text=NOTIFICATIONS["RU"]["no_bookmarks"])


@router.callback_query(Text(text='forward'))
async def process_forward_command(callback: CallbackQuery):
    """
    This handler will be triggered by pressing the inline "forward" button
    """
    if users_db[callback.from_user.id]['page'] < len(book):
        await _page_switching(callback, 1)
    await callback.answer()


@router.callback_query(Text(text='backward'))
async def process_backward_command(callback: CallbackQuery):
    """
    This handler will be triggered by pressing the inline "backward" button
    """
    if users_db[callback.from_user.id]['page'] > 1:
        await _page_switching(callback, -1)
    await callback.answer()


# page switching
async def _page_switching(cb: CallbackQuery, direction: int):
    """
    Switching pages on click "forward" or "backward" buttons
    :param direction: "1" when "forward" and "-1" when "backward"
    """
    users_db[cb.from_user.id]['page'] += direction
    text = book[users_db[cb.from_user.id]['page']]
    await cb.message.edit_text(
        text=text,
        reply_markup=_cr_pg_kb(cb))


@router.callback_query(lambda x: '/' in x.data and
                                 x.data.replace('/', '').isdigit())
async def process_page_press(callback: CallbackQuery):
    """
    This handler will be triggered by pressing the inline button with
    the current page number and add the current page to bookmarks
    """
    users_db[callback.from_user.id]['bookmarks'].add(
        users_db[callback.from_user.id]['page'])
    await callback.answer(NOTIFICATIONS["RU"]["added_bookmarks"])


@router.callback_query(IsDigitCallbackData())
async def process_bookmark_press(callback: CallbackQuery):
    """
    This handler will be triggered by pressing an inline button with
    a bookmark from the list of bookmarks
    """
    text = book[int(callback.data)]
    users_db[callback.from_user.id]['page'] = int(callback.data)
    await callback.message.edit_text(
        text=text,
        reply_markup=_cr_pg_kb(callback))
    await callback.answer()


@router.callback_query(Text(text='edit_bookmarks'))
async def process_edit_press(callback: CallbackQuery):
    """
    This handler will be triggered by pressing the inline "edit_bookmarks"
    button below the list of bookmarks
    """
    await callback.message.edit_text(
        text=NOTIFICATIONS["RU"][callback.data],
        reply_markup=create_edit_keyboard(
            *users_db[callback.from_user.id]["bookmarks"]))
    await callback.answer()


@router.callback_query(Text(text='cancel'))
async def process_cancel_press(callback: CallbackQuery):
    """
    This handler will be triggered by pressing the inline "cancel" button
    while working with the list of bookmarks (viewing and editing)
    """
    await callback.message.edit_text(
        text=NOTIFICATIONS["RU"]["cancel_text"])
    await callback.answer()


@router.callback_query(IsDelBookmarksCallbackData())
async def process_del_bookmark_press(callback: CallbackQuery):
    """
    This handler will be triggered by pressing an inline button with
    a bookmark from the list of bookmarks to be deleted
    """
    users_db[callback.from_user.id]['bookmarks'].remove(
        int(callback.data[:-3]))
    if users_db[callback.from_user.id]['bookmarks']:
        await callback.message.edit_text(
            text=NOTIFICATIONS["RU"]['bookmarks'],
            reply_markup=create_edit_keyboard(
                *users_db[callback.from_user.id]["bookmarks"]))
    else:
        await callback.message.edit_text(
            text=NOTIFICATIONS["RU"]['no_bookmarks'])
    await callback.answer()

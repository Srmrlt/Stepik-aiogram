from dataclasses import dataclass

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# @dataclass
class GoodsCallbackFactory(CallbackData, prefix='goods'):
    category_id: int
    subcategory_id: int
    item_id: int


btn_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Kat 1',
    callback_data=GoodsCallbackFactory(
        category_id=1,
        subcategory_id=0,
        item_id=0).pack())

btn_2: InlineKeyboardButton = InlineKeyboardButton(
    text='Kat 2',
    callback_data=GoodsCallbackFactory(
        category_id=2,
        subcategory_id=0,
        item_id=0).pack())

keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[btn_1], [btn_2]])

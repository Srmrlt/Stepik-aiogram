from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON_RU

# Keyboard yes/no
yes_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
no_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[[yes_btn, no_btn]],
                                                     resize_keyboard=True,
                                                     one_time_keyboard=True)

# Keyboard rock-scissors-paper
rock_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
scissors_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
paper_btn: KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

rsp_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
rsp_builder.row(rock_btn, scissors_btn, paper_btn, width=1)

rsp_kb = ReplyKeyboardMarkup = rsp_builder.as_markup(resize_keyboard=True)

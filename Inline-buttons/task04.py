from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F

from config_data.config import Config, load_config
from callback_data_factory import keyboard, GoodsCallbackFactory

config: Config = load_config()
bot: Bot = Bot(token=config.tg_bot.token,
               parse_mode='HTML')
dp: Dispatcher = Dispatcher()


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Keyboard',
                         reply_markup=keyboard)


@dp.callback_query(GoodsCallbackFactory.filter(F.item_id == 0))
async def process_category_press(callback: CallbackQuery,
                                 callback_data: GoodsCallbackFactory):
    await callback.message.answer(text=callback_data.pack())
    await callback.answer()


@dp.callback_query()
async def process_any_inline_button_press(callback: CallbackQuery):
    print(callback.json(indent=4, exclude_none=True))


if __name__ == '__main__':
    dp.run_polling(bot)

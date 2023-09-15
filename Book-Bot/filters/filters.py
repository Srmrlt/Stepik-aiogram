from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class IsDigitCallbackData(BaseFilter):
    """
    determines if the data is a string consisting of numbers
    """
    async def __call__(self, callback: CallbackQuery) -> bool:
        return isinstance(callback.data, str) and callback.data.isdigit()


class IsDelBookmarksCallbackData(BaseFilter):
    """
    determines if the data is a string containing a "delete" button
    and ending with numbers
    """
    async def __call__(self, callback: CallbackQuery) -> bool:
        st1 = isinstance(callback.data, str)
        st2 = 'del' in callback.data
        st3 = callback.data[:-3].isdigit()
        return st1 and st2 and st3

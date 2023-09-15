from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.lexicon import MENU_COMMANDS


async def set_main_menu(bot: Bot):
    """
    Function to customize the Menu button of the bot
    """
    main_menu_commands = [BotCommand(command=command, description=description)
                          for command, description
                          in MENU_COMMANDS['RU'].items()]
    await bot.set_my_commands(main_menu_commands)

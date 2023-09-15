import random
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Text, Command


bot_api_token: str = '6293522184:AAGp9WalX-8pBafVLYFYt6NFB0eQMN743nE'

user: dict = {
    'in_game': False,
    'secret_number': None,
    'attempts': None,
    'total_games': 0,
    'wins': 0
}
max_attempts: int = 5

bot: Bot = Bot(token=bot_api_token)
dp: Dispatcher = Dispatcher()


def get_random_number() -> int:
    return random.randint(1, 100)


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer("Hi!\n"
                         "You can play a game: Guess the number! Good luck!\n"
                         "Type 'yes' to start\n"
                         "/help for rules")


@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer("I should have typed the rules here but I'm too lazy\n"
                         "Guess the number from 1 to 100\n"
                         "You have 5 attempts\n"
                         "Type 'yes' to start")


@dp.message(Command(commands=["stat"]))
async def process_stat_command(message: Message):
    await message.answer(f"All games: {user['total_games']}\n"
                         f"Winn games: {user['wins']}")


@dp.message(Command(commands=["stop"]))
async def process_stop_command(message: Message):
    if user['in_game']:
        await message.answer("Game is ended")
        user['in_game'] = False
    else:
        await message.answer("We are not playing yet\n"
                             "Type 'yes' to start")


@dp.message(Text(text=['yes'], ignore_case=True))
async def game_start_command(message: Message):
    if user['in_game']:
        await message.answer("You're already playing\n"
                             "To end game type '/stop'")
    else:
        await message.answer("Let's play!!!")
        user['in_game'] = True
        user['attempts'] = max_attempts
        user['secret_number'] = get_random_number()
        print(user['secret_number'])
        user['total_games'] += 1


@dp.message()
async def main_logic(message: Message):
    if user['in_game']:
        try:
            number = int(message.text)
            await game_guess_number(message, number)
        except ValueError:
            await message.answer("We are in the GAME, here are my rules.\n"
                                 "Enter NUMBER")
    else:
        await message.answer("I don't know this command, try another one")


async def game_guess_number(message: Message, number: int):
    if user['secret_number'] == number:
        await message.answer("You win")
        user['wins'] += 1
        user['in_game'] = False
    elif user['secret_number'] > number:
        await message.answer("My number is bigger")
        await loser(message)
    elif user['secret_number'] < number:
        await message.answer("My number is lower")
        await loser(message)


async def loser(message: Message):
    user['attempts'] -= 1
    if user['attempts']:
        await message.answer(f"You have {user['attempts']}")
    else:
        await message.answer("You lose\n"
                             "Another try? Type 'yes'")
        user['in_game'] = False


if __name__ == '__main__':
    dp.run_polling(bot)

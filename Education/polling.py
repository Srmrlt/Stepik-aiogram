import requests
import time


api_url: str = 'https://api.telegram.org/bot'
bot_token: str = '6293522184:AAGp9WalX-8pBafVLYFYt6NFB0eQMN743nE'
offset: int = -2
timeout: float = 6.2
updates: dict


def do_something() -> None:
    print('Update!!!')


while True:
    start_time = time.time()
    updates = requests.get(f'{api_url}{bot_token}/getUpdates?offset={offset + 1}&timeout={timeout}').json()
    # updates = requests.get(f'{api_url}{bot_token}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something()

    end_time = time.time()
    print(f'Time between questions to Telegram Bot API: {end_time - start_time}')

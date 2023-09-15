import requests
import time


api_url: str = 'https://api.telegram.org/bot'
bot_token: str = '6293522184:AAGp9WalX-8pBafVLYFYt6NFB0eQMN743nE'
text: str = 'Hi, glad to see you! :)'

offset: int = -2

for counter in range(10):
    print(f"i'm alive {counter}")

    updates = requests.get(f'{api_url}{bot_token}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f"{api_url}{bot_token}/sendMessage?chat_id={chat_id}&text={text}")

    time.sleep(1)

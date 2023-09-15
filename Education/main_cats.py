import requests
from time import sleep


api_url: str = 'https://api.telegram.org/bot'
bot_token: str = '6293522184:AAGp9WalX-8pBafVLYFYt6NFB0eQMN743nE'
text: str = 'Hi, glad to see you! :)'

# api_cats_url: str = 'https://api.thecatapi.com/v1/images/search'
# api_cats_url: str = 'https://randomfox.ca/floof/'
api_cats_url: str = 'https://random.dog/woof.json'
error_text: str = 'ups, we lost the cat :('

offset: int = -2

cat_response: requests.Response
cat_link: str

for counter in range(50):
    print(f"i'm alive {counter}")
    updates = requests.get(f'{api_url}{bot_token}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(api_cats_url)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()['url']
                requests.get(f"{api_url}{bot_token}/sendPhoto?chat_id={chat_id}&photo={cat_link}")
            else:
                requests.get(f"{api_url}{bot_token}/sengMessage?chat_id={chat_id}&text={error_text}")
    sleep(0.5)

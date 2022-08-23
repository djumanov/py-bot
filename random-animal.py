import requests
import telegram
import os

TOKEN = os.environ['TOKEN']
bot   = telegram.Bot(token=TOKEN)


def keyboard():
    return [[telegram.KeyboardButton('random 🐶')], [telegram.KeyboardButton('random 😺')]]


def get_dog():
    url = 'https://random.dog/woof.json'
    r   = requests.get(url)

    return r.json()['url']


def get_cat():
    url = 'https://aws.random.cat/meow'
    r   = requests.get(url=url)

    return r.json()['file']



def main():
    last_update    = bot.getUpdates()[-1]
    last_update_id = last_update.update_id

    while True:
        curr_update    = bot.getUpdates()[-1]
        curr_update_id = curr_update.update_id

        if last_update_id != curr_update_id:
            chat_id = curr_update.message.from_user.id

            text    = curr_update.message.text
            if text == '/start':
                bot.send_message(chat_id, 'welocome!', reply_markup=telegram.ReplyKeyboardMarkup(keyboard=keyboard()))
            elif text == 'random 🐶':
                bot.send_photo(chat_id, get_dog())
            elif text == 'random 😺':
                bot.send_photo(chat_id, get_cat())
            else:
                bot.send_message(chat_id, 'select button | random 🐶 or random 😺')
            
            last_update_id = curr_update_id

main()
# registration form


# start

# welcome message
# likes or dislikes

# database db.json


import json
import os
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    CallbackContext,
    Filters,
)
from telegram import Update


TOKEN = os.environ['TOKEN']

updater    = Updater(token=TOKEN)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    msg     = update.message
    from_user = msg.from_user

    with open(file='db.json') as db:
        str_data = db.read()
    if str_data:
        json_data: dict = json.loads(str_data)
        if from_user.id not in [u['user_id'] for u in json_data['result']]:
            new_user = {
                'user_name': from_user.full_name,
                'user_id': from_user.id,
                'like': 0,
                'dislike': 0,
            }
            json_data['result'].append(new_user)

            str_data = json.dumps(json_data, input=4)
            with open(file='db.json', mode='w') as r_db:
                r_db.write(str_data)
    else:
        base_db = {
            'result': []
        }
        new_user = {
            'user_name': from_user.full_name,
            'user_id': from_user.id,
            'like': 0,
            'dislike': 0,
        }
        base_db['result'].append(new_user)

        str_data = json.dumps(base_db, indent=4)
        with open(file='db.json', mode='w') as r_db:
            r_db.write(str_data)

    msg.reply_text('Welcome to bot!\n\nsend 👍 or 👎?')



def send_result(update: Update, context: CallbackContext):
    msg  = update.message
    text = msg.text
    chat_id = msg.from_user.id

    with open(file='db.json') as db:
        json_data = json.loads(db.read())

    if text == '👍' or text == '👎':
        for user in json_data['result']:
            if user['user_id'] == chat_id:
                is_user = True
                likes = user['like']
                dislikes = user['dislike']
                if text == '👍':
                    user['like'] += 1
                    likes += 1
                    break
                else:
                    user['dislike'] += 1
                    dislikes += 1
                    break
        
        with open(file='db.json', mode='w') as r_db:
            json.dump(json_data, r_db, indent=4)
        
        msg.reply_text(f'likes: {likes}\ndislikes: {dislikes}')
    else:
        msg.reply_text('send 👍 or 👎, please?')
    
    

dispatcher.add_handler(handler=CommandHandler(command='start', callback=start))
dispatcher.add_handler(handler=MessageHandler(Filters.text, callback=send_result))

updater.start_polling()
updater.idle()
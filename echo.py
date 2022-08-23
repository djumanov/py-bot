import telegram
import os

TOKEN = os.environ['TOKEN']
bot   = telegram.Bot(token=TOKEN)

def main():
    last_update    = bot.getUpdates()[-1]
    last_update_id = last_update.update_id

    while True:
        curr_update    = bot.getUpdates()[-1]
        curr_update_id = curr_update.update_id

        if last_update_id != curr_update_id:
            chat_id = curr_update.message.from_user.id

            text    = curr_update.message.text
            if text:
                bot.send_message(chat_id, text)
            
            photos = curr_update.message.photo
            if photos:
                file_id = photos[-1].file_id
                bot.send_photo(chat_id, file_id)

            document = curr_update.message.document
            if document:
                file_id = document.file_id
                bot.send_document(chat_id, file_id)

            video = curr_update.message.video
            if video:
                file_id = video.file_id
                bot.send_video(chat_id, file_id)

            voice = curr_update.message.voice
            if voice:
                file_id = voice.file_id
                bot.send_voice(chat_id, file_id)
            
            last_update_id = curr_update_id

main()
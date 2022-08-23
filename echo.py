import telegram
import os

TOKEN = os.environ['TOKEN']

bot = telegram.Bot(token=TOKEN)
updates = bot.getUpdates()
for update in updates:
    print(update)
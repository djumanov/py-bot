import telegram
import os

TOKEN = os.environ['TOKEN']

bot = telegram.Bot(token=TOKEN)
print(bot.getMe())
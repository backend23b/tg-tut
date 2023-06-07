from telegram import Bot
import os

TOKEN = os.environ.get('TOKEN')

bot = Bot(token=TOKEN)

user = bot.getMe()
print(user.id)
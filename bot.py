from telegram import Bot
import os

TOKEN = os.environ.get('TOKEN')

bot = Bot(token=TOKEN)

chat_id = '1258594598'
text = 'salom'

bot.sendMessage(chat_id=chat_id, text=text)
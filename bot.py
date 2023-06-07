from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import Update
import os
import time

TOKEN = os.environ.get('TOKEN')

def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    text = 'salom xush kelipsiz'

    context.bot.sendMessage(chat_id, text)

def echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    text = update.message.text

    context.bot.sendMessage(chat_id, text)


updater = Updater(token=TOKEN)
dp = updater.dispatcher

dp.add_handler(handler=CommandHandler(command='start', callback=start))
dp.add_handler(handler=MessageHandler(filters=Filters.text, callback=echo))

updater.start_polling()
updater.idle()
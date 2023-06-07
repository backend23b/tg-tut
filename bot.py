from telegram import Bot
import os
import time

TOKEN = os.environ.get('TOKEN')

bot = Bot(token=TOKEN)

last_update_id = bot.getUpdates()[-1].update_id
while True:
    time.sleep(1)

    curr_update = bot.getUpdates()[-1]

    if last_update_id != curr_update.update_id:
        chat_id = curr_update.message.chat.id
        text    = curr_update.message.text

        bot.sendMessage(chat_id=chat_id, text=text)

        last_update_id = curr_update.update_id
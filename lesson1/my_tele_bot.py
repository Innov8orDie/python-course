import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    updater = Updater("532830261:AAEOf0x0wJigcKy1tZ1quRV-3dySxcq3SKg")

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def main():
    updater = Updater("532830261:AAEOf0x0wJigcKy1tZ1quRV-3dySxcq3SKg")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", greet_user))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    updater.start_polling()    
    updater.idle()

def greet_user(bot, update):
    print('Hi!')
    update.message.reply_text('Here I am, wanna talk?')

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

main()
import telebot

bot = telebot.TeleBot("893162503:AAGwD5FvkRYYs297kEMkI_wvI0gdbaG6p7Y")

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
import telebot

bot = telebot.TeleBot('8033276251:AAFc3M82s3P8plaI-ZgNgtg7ofAK4dH52ps')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat_id, "привет я бот")

# Запуск бота
bot.polling(non_stop=True)
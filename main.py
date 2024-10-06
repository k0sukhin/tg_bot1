import telebot

bot = telebot.TeleBot('7505931690:AAEmlFx2JFy6lHf6t_80Bd_mqLlXatUqTjs')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, message)


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, 'Не надо тебе этого')


bot.polling(none_stop=True)





# def start(m, res=False):
#     bot.send_message(m.chat.id, 'Вы вошли телеграм бот второй квартиры')


# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


# bot.polling(none_stop=True, interval=0)

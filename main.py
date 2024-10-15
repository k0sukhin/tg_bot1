import telebot
from telebot import types


bot = telebot.TeleBot('7505931690:AAEmlFx2JFy6lHf6t_80Bd_mqLlXatUqTjs')


@bot.message_handler(commands=['start'])
def main_menu(message):

    inline_keyboard = types.InlineKeyboardMarkup()
    inline_keyboard.add(
        types.InlineKeyboardButton(
            'Информация об авто', callback_data='car_info'))

    inline_keyboard.add(
        types.InlineKeyboardButton(
            'Список комплектующих', callback_data='car_info'))

    bot.send_message(
        message.chat.id, '---Здесь должен быть приветственный текст---',
        reply_markup=inline_keyboard)


bot.polling(none_stop=True)

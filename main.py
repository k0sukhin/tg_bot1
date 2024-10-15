import telebot
from telebot import types
from texts import main_menu_text
from classes import Car


bot = telebot.TeleBot('7505931690:AAEmlFx2JFy6lHf6t_80Bd_mqLlXatUqTjs')
auto = Car()
flag = False


@bot.message_handler(commands=['start'])
def main_menu(message):
    main_menu_keyboard = types.InlineKeyboardMarkup()
    main_menu_keyboard.add(
        types.InlineKeyboardButton(
            'Информация об авто', callback_data='car_info'))

    main_menu_keyboard.add(
        types.InlineKeyboardButton(
            'Изменить информацию об авто', callback_data='update_car_info'))

    main_menu_keyboard.add(
        types.InlineKeyboardButton(
            'Список комплектующих', callback_data='details_info'))

    main_menu_keyboard.add(
        types.InlineKeyboardButton(
            'Добавить комплектующее', callback_data='add_details'))

    bot.send_message(
        message.chat.id, main_menu_text, reply_markup=main_menu_keyboard)


@bot.message_handler(content_types=['text'])
def get_mark(message):
    mrk = bot.send_message(
        message.chat.id,
        'Введите марку авто:')
    bot.register_next_step_handler(mrk, func)


@bot.message_handler(content_types=['text'])
def get_model(message):
    mdl = bot.send_message(
        message.chat.id,
        'Введите модель авто:')
    bot.register_next_step_handler(mdl, func1)


@bot.message_handler(content_types=['text'])
def get_year_of_manufacture(message):
    yom = bot.send_message(
        message.chat.id,
        'Введите год выпуска авто:')
    bot.register_next_step_handler(yom, func2)


@bot.message_handler(content_types=['text'])
def get_mileage(message):
    mile = bot.send_message(
        message.chat.id,
        'Введите пробег авто:')
    bot.register_next_step_handler(mile, func3)


@bot.callback_query_handler(func=lambda call: True)
def car_info_menu(call):
    if call.message:
        if call.data == 'car_info':
            global flag
            if not flag:
                bot.send_message(call.message.chat.id,
                                 'Информация отсутствует')
                get_mark(call.message)

                flag = True
            else:
                bot.send_message(call.message.chat.id,
                                 'Информация об авто:')
                bot.send_message(call.message.chat.id,
                                 f'Марка авто - {auto.mark}')
                bot.send_message(call.message.chat.id,
                                 f'Модель авто - {auto.model}')
                bot.send_message(call.message.chat.id,
                                 f'Год выпуска авто - {auto.year_of_manufacture}')
                bot.send_message(call.message.chat.id,
                                 f'Пробег авто - {auto.mileage}')

        elif call.data == 'back':
            bot.delete_message(chat_id=call.message.chat.id,
                               message_id=call.message.id)

            main_menu(call.message)


def func(message):
    auto.mark = message.text
    get_model(message)


def func1(message):
    auto.model = message.text
    get_year_of_manufacture(message)


def func2(message):
    auto.year_of_manufacture = message.text
    get_mileage(message)


def func3(message):
    auto.mileage = message.text

    car_info_menu_keyboard = types.InlineKeyboardMarkup()
    car_info_menu_keyboard.add(
        types.InlineKeyboardButton(
            'Назад', callback_data='back'))

    bot.send_message(
        message.chat.id,
        'Информация успешно введена',
        reply_markup=car_info_menu_keyboard)


if __name__ == "__main__":
    bot.polling(none_stop=True)

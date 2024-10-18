import telebot
from telebot import types
from texts import main_menu_text
from classes import Car


bot = telebot.TeleBot('7505931690:AAEmlFx2JFy6lHf6t_80Bd_mqLlXatUqTjs')
auto = Car()
flag = False
details_list = []


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
                                 f"Информация об авто:\n"
                                 f"Марка - {auto.mark}\n"
                                 f"Модель - {auto.model}\n"
                                 f"Год выпуска - {auto.year_of_manufacture}\n"
                                 f"Пробег - {auto.mileage}\n")

        elif call.data == 'back':
            bot.delete_message(chat_id=call.message.chat.id,
                               message_id=call.message.id)

            main_menu(call.message)

        elif call.data == 'update_car_info':
            update_mileage = bot.send_message(call.message.chat.id,
                                              'Введите новый пробег:')
            bot.register_next_step_handler(update_mileage, update_mileage_func)

        elif call.data == 'details_info':
            if details_list == []:
                bot.send_message(call.message.chat.id, 'Комплектующие не добавлены')
            else:
                bot.send_message(call.message.chat.id, details_list)


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


def update_mileage_func(message):
    auto.mileage_update(message.text)
    bot.send_message(
        message.chat.id,
        'Пробег успешно обновлен')


if __name__ == "__main__":
    bot.polling(none_stop=True)

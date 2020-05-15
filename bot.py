# -*- coding: utf-8 -*-

import telebot
import config
import shelve
import disciplines
from datetime import datetime, date
from telebot import types

token = ''
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def welcome(message):
    podgrkey = types.InlineKeyboardMarkup()
    podgr1 = types.InlineKeyboardButton(text='1', callback_data='podgr1')
    podgr2 = types.InlineKeyboardButton(text='2', callback_data='podgr2')
    podgrkey.add(podgr1, podgr2)

    bot.send_message(message.chat.id, config.salaam, reply_markup=podgrkey)

    config.put_in_object(message.from_user.id, message.from_user.first_name,
                         message.from_user.last_name, message.from_user.username)


@bot.message_handler(func=lambda message: message.text.lower() == 'начать сначала')
def reset(message):
    podgrkey = types.InlineKeyboardMarkup()
    podgr1 = types.InlineKeyboardButton(text='1', callback_data='podgr1')
    podgr2 = types.InlineKeyboardButton(text='2', callback_data='podgr2')
    podgrkey.add(podgr1, podgr2)

    bot.send_message(message.chat.id, config.salaam, reply_markup=podgrkey)

    config.put_in_object(message.from_user.id, message.from_user.first_name,
                         message.from_user.last_name, message.from_user.username)


@bot.message_handler(func=lambda message: message.text.lower() == 'дай ссылку')
def givelink(message):
    today = datetime.now()
    hour = today.hour + 3  # +3 потому что на сервере время UTC+0
    minute = today.minute
    study_time = hour * 60 + minute
    day = datetime.weekday(today)
    week = date(today.year, today.month, today.day).isocalendar()[1]

    pd = shelve.open('podgrupp')
    user_subgroup = pd.get(str(message.chat.id), default='3')
    pd.close()

    discipline_index = 0
    z = True
    t = True

    if user_subgroup != '1' and user_subgroup != '2':
        z = False

    key = types.InlineKeyboardMarkup()
    ############################    Понедельник    #################################
    if day == 0:
        if 585 <= study_time <= 639:
            key.add(disciplines.disciplines_links["discreteMath"])
            discipline_index = 0
        elif 640 <= study_time <= 745:
            key.add(disciplines.disciplines_links["AZAMAT"])

            discipline_index = 2
        else:
            t = False
    ##############################  Вторник    #####################################
    elif day == 1:
        if 500 <= study_time <= 584:
            if user_subgroup == '1':
                key.add(disciplines.disciplines_links["english_subgroup_1"])
                discipline_index = 4
            elif user_subgroup == '2':
                key.add(disciplines.disciplines_links["AZAMAT"])
                discipline_index = 3
        elif 585 <= study_time <= 639:
            key.add(disciplines.disciplines_links["discreteMath"])
            discipline_index = 1
        elif 640 <= study_time <= 694:
            if week == 20 or week == 22 or week == 24:
                key.add(disciplines.disciplines_links["history"])
                discipline_index = 6
            elif week == 21 or week == 23 or week == 25:
                key.add(disciplines.disciplines_links["lifeSafety"])
                discipline_index = 8
        else:
            t = False
    ############################    Среда    ##################################
    elif day == 2:
        if 500 <= study_time <= 584:
            if week == 20 or week == 22 or week == 24:
                key.add(disciplines.disciplines_links["history"])
                discipline_index = 5
            elif week == 21 or week == 23 or week == 25:
                key.add(disciplines.disciplines_links["lifeSafety"])
                discipline_index = 7
        elif 585 <= study_time <= 639:
            if week == 20 or week == 22 or week == 24:
                key.add(disciplines.disciplines_links["cheCultureAndEthics"])
                discipline_index = 9
            elif week == 21 or week == 23 or week == 25:
                key.add(disciplines.disciplines_links["cheHistory"])
                discipline_index = 10
        elif 640 <= study_time <= 694:
            if user_subgroup == '1':
                t = False
            elif user_subgroup == '2':
                key.add(disciplines.disciplines_links["english_subgroup_2"])
                discipline_index = 4
        else:
            t = False
    ############################    Четверг    ################################
    elif day == 3:  # Четверг
        if 500 <= study_time <= 584:
            key.add(disciplines.disciplines_links["mathAnalysis"])
            discipline_index = 12
        elif 585 <= study_time <= 639:
            key.add(disciplines.disciplines_links["mathAnalysis"])
            discipline_index = 11
        elif 640 <= study_time <= 694:
            if user_subgroup == '1':
                key.add(disciplines.disciplines_links["AZAMAT"])
                discipline_index = 3
            elif user_subgroup == '2':
                t = False
        else:
            t = False
    ############################    Пятница    ################################
    # Выходной
    ############################    Суббота    ################################
    elif day == 5:
        if 500 <= study_time <= 584:
            key.add(disciplines.disciplines_links["probabilityTheory"])
            discipline_index = 13
        elif 585 <= study_time <= 639:
            key.add(disciplines.disciplines_links["introToSE"])
            discipline_index = 14
        elif 640 <= study_time <= 694:
            if user_subgroup == '1':
                key.add(disciplines.disciplines_links["introToSE"])
                discipline_index = 15
            elif user_subgroup == '2':
                t = False
        elif 695 <= study_time <= 745:
            if user_subgroup == '1':
                t = False
            elif user_subgroup == '2':
                key.add(disciplines.disciplines_links["introToSE"])
                discipline_index = 15
        else:
            t = False
    ###########################################################################
    else:
        t = False
    ###########################################################################
    if not z:
        bot.send_message(message.chat.id, config.no_subgroup, parse_mode='HTML')
    elif not t:
        bot.send_message(message.chat.id, config.chill)
    else:
        bot.send_message(message.chat.id, disciplines.disciplines_out_list[discipline_index], reply_markup=key)

    config.put_in_object(message.from_user.id, message.from_user.first_name, message.from_user.last_name,
                         message.from_user.username, hours=hour, minutes=minute)


@bot.message_handler(func=lambda message: message.text.lower() == 'полный список пар')
def full_list(message):
    bot.send_message(message.chat.id, disciplines.disciplines_list, parse_mode='MarkdownV2')


@bot.message_handler(func=lambda message: message.text.lower() == 'расписание')
def ra(message):
    bot.send_document(message, disciplines.disciplines_list, timeout=5)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    dai = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Дай ссылку')
    button2 = types.KeyboardButton(text='Полный список пар')
    button3 = types.KeyboardButton(text='Расписание')
    button4 = types.KeyboardButton(text='Начать сначала')
    dai.row(button1)
    dai.row(button2, button3)
    dai.row(button4)

    if call.data == 'podgr1':
        pd = shelve.open('podgrupp')
        pd[str(call.from_user.id)] = '1'  # в хранилище записываем значение '1' для ключа 'айди юзера'
        pd.close()
        bot.answer_callback_query(call.id, "Answer is 1")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Подгруппа №1. Отлично, идём дальше :)')
    elif call.data == 'podgr2':
        pd = shelve.open('podgrupp')
        pd[str(call.from_user.id)] = '2'  # в хранилище записываем значение '2' для ключа 'айди юзера'
        pd.close()
        bot.answer_callback_query(call.id, "Answer is 2")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Подгруппа №2. Отлично, идём дальше :)')

    bot.send_message(call.message.chat.id, text=config.help, reply_markup=dai, parse_mode='HTML')

@bot.message_handler(commands=['rasp'])
def find_file_ids(message):
    f = open('raspisanie.jpg', 'rb')
    img = bot.send_document(message.chat.id, f, timeout=5)
    bot.send_message(message.chat.id, img.document.file_id, reply_to_message_id=img.message_id)
if __name__ == '__main__':
    bot.infinity_polling()

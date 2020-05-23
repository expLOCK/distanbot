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
        if 600 <= study_time <= 669:
            key.add(disciplines.disciplines_links["discreteMath"])
            discipline_index = 0
        elif 670 <= study_time <= 739:
            key.add(disciplines.disciplines_links["AZAMAT"])
            discipline_index = 2
        elif 740 <= study_time <= 789:
            key.add(disciplines.disciplines_links["break"])
            discipline_index = 16
        elif 790 <= study_time <= 859:
            key.add(disciplines.disciplines_links["AZAMAT"])
            discipline_index = 2
        else:
            t = False
    ##############################  Вторник    #####################################
    elif day == 1:
        if 500 <= study_time <= 599:
            if user_subgroup == '1':
                key.add(disciplines.disciplines_links["english_subgroup_1"])
                discipline_index = 4
            elif user_subgroup == '2':
                key.add(disciplines.disciplines_links["AZAMAT"])
                discipline_index = 3
        elif 600 <= study_time <= 669:
            key.add(disciplines.disciplines_links["discreteMath"])
            discipline_index = 1
        elif 670 <= study_time <= 739:
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
        if 500 <= study_time <= 599:
            if week == 20 or week == 22 or week == 24:
                key.add(disciplines.disciplines_links["history"])
                discipline_index = 5
            elif week == 21 or week == 23 or week == 25:
                key.add(disciplines.disciplines_links["lifeSafety"])
                discipline_index = 7
        elif 600 <= study_time <= 669:
            if week == 20 or week == 22 or week == 24:
                key.add(disciplines.disciplines_links["cheCultureAndEthics"])
                discipline_index = 9
            elif week == 21 or week == 23 or week == 25:
                key.add(disciplines.disciplines_links["cheHistory"])
                discipline_index = 10
        elif 670 <= study_time <= 739:
            if user_subgroup == '1':
                t = False
            elif user_subgroup == '2':
                key.add(disciplines.disciplines_links["english_subgroup_2"])
                discipline_index = 4
        else:
            t = False
    ############################    Четверг    ################################
    elif day == 3:  # Четверг
        if 500 <= study_time <= 599:
            key.add(disciplines.disciplines_links["mathAnalysis"])
            discipline_index = 12
        elif 600 <= study_time <= 669:
            key.add(disciplines.disciplines_links["mathAnalysis"])
            discipline_index = 11
        elif 670 <= study_time <= 739:
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
        if 500 <= study_time <= 599:
            key.add(disciplines.disciplines_links["probabilityTheory"])
            discipline_index = 13
        elif 600 <= study_time <= 669:
            key.add(disciplines.disciplines_links["introToSE"])
            discipline_index = 14
        elif 670 <= study_time <= 739:
            if user_subgroup == '1':
                key.add(disciplines.disciplines_links["introToSE"])
                discipline_index = 15
            elif user_subgroup == '2':
                t = False
        elif 740 <= study_time <= 789:
            key.add(disciplines.disciplines_links["break"])
            discipline_index = 16
        elif 790 <= study_time <= 859:
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
        bot.send_message(message.chat.id, config.get_discipline(discipline_index), reply_markup=key)


@bot.message_handler(func=lambda message: message.text.lower() == 'полный список пар')
def full_list(message):
    bot.send_message(message.chat.id, disciplines.disciplines_list, parse_mode='MarkdownV2')


@bot.message_handler(func=lambda message: message.text.lower() == 'расписание')
def ra(message):
    bot.send_document(message.chat.id, config.raspisanie, timeout=5)


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
    break_flag = False

    if call.data == 'podgr1':
        pd = shelve.open('podgrupp')
        pd[str(call.from_user.id)] = '1'
        pd.close()
        bot.answer_callback_query(call.id, "Answer is 1")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Подгруппа №1. Отлично, идём дальше :)')
    elif call.data == 'podgr2':
        pd = shelve.open('podgrupp')
        pd[str(call.from_user.id)] = '2'
        pd.close()
        bot.answer_callback_query(call.id, "Answer is 2")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Подгруппа №2. Отлично, идём дальше :)')
    elif call.data == 'good':
        bot.answer_callback_query((call.id, '👍'))
        break_flag = True

    if not break_flag:
        bot.send_message(call.message.chat.id, text=config.help, reply_markup=dai, parse_mode='HTML')


if __name__ == '__main__':
    bot.infinity_polling()

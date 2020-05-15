# -*- coding: utf-8 -*-

import telebot
import config
import shelve
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

    bot.send_message(message.chat.id, config.salam, reply_markup=podgrkey)

    config.put_in_object(message.from_user.id, message.from_user.first_name,
                         message.from_user.last_name, message.from_user.username)


@bot.message_handler(func=lambda message: message.text.lower() == 'начать сначала')
def reset(message):
    podgrkey = types.InlineKeyboardMarkup()
    podgr1 = types.InlineKeyboardButton(text='1', callback_data='podgr1')
    podgr2 = types.InlineKeyboardButton(text='2', callback_data='podgr2')
    podgrkey.add(podgr1, podgr2)

    bot.send_message(message.chat.id, config.salam, reply_markup=podgrkey)


@bot.message_handler(func=lambda message: message.text.lower() == 'дай ссылку')
def givelink(message):
    today = datetime.now()
    hour = today.hour + 3  # +3 потому что на сервере время UTC+0
    minute = today.minute
    vremya = hour * 60 + minute
    day = datetime.weekday(today)
    nedelya = date(today.year, today.month, today.day).isocalendar()[1]

    pd = shelve.open('podgrupp')
    podgruppa = pd.get(str(message.chat.id), default='3')
    pd.close()

    x = 0
    z = True
    t = True

    if podgruppa != '1' and podgruppa != '2':
        z = False

    key = types.InlineKeyboardMarkup()
    azamat = types.InlineKeyboardButton(text='Подключиться', url="https://chesuru.webex.com/meet/")
    vvedenie = types.InlineKeyboardButton(text='Подключиться', url="https://chesuru.webex.com/meet/")
    history = types.InlineKeyboardButton(text='Подключиться', url="https://chesuru.webex.com/meet/")
    bjd = types.InlineKeyboardButton(text='Подключиться', url="https://chesuru.webex.com/meet/")
    eng1 = types.InlineKeyboardButton(text='Подключиться', url="https://chesuru.webex.com/meet/")
    eng2 = types.InlineKeyboardButton(text='Подключиться', url="https://chesuru.webex.com/meet/")
    matan = types.InlineKeyboardButton(text='Подключиться', url="https://chesuru.webex.com/meet/")
    terver = types.InlineKeyboardButton(text='Подключиться', url="https://chesuru.webex.com/meet/")
    diskra = types.InlineKeyboardButton(text='Подключиться', url="https://chesuru.webex.com/meet/")
    history95 = types.InlineKeyboardButton(text='Подключиться', url="https://chesuru.webex.com/meet/")
    etika = types.InlineKeyboardButton(text='Подключиться', url="https://chesuru.webex.com/meet/")
    if day == 0:  # Понедельник
        if 585 <= vremya <= 639:
            key.add(diskra)
            x = 0
        elif 640 <= vremya <= 745:
            key.add(azamat)
            x = 2
        else:
            t = False
    elif day == 1:  # Вторник
        if 500 <= vremya <= 584:
            if podgruppa == '1':
                key.add(eng1)
                x = 4
            elif podgruppa == '2':
                key.add(azamat)
                x = 3
        elif 585 <= vremya <= 639:
            key.add(diskra)
            x = 1
        elif 640 <= vremya <= 694:
            if nedelya == 20 or nedelya == 22 or nedelya == 24:
                key.add(history)
                x = 6
            elif nedelya == 21 or nedelya == 23 or nedelya == 25:
                key.add(bjd)
                x = 8
        else:
            t = False
    elif day == 2:  # Среда
        if 500 <= vremya <= 584:
            if nedelya == 20 or nedelya == 22 or nedelya == 24:
                key.add(history)
                x = 5
            elif nedelya == 21 or nedelya == 23 or nedelya == 25:
                key.add(bjd)
                x = 7
        elif 585 <= vremya <= 639:
            if nedelya == 20 or nedelya == 22 or nedelya == 24:
                key.add(etika)
                x = 9
            elif nedelya == 21 or nedelya == 23 or nedelya == 25:
                key.add(history95)
                x = 10
        elif 640 <= vremya <= 694:
            if podgruppa == '1':
                t = False
            elif podgruppa == '2':
                key.add(eng2)
                x = 4
        else:
            t = False
    elif day == 3:  # Четверг
        if 500 <= vremya <= 584:
            key.add(matan)
            x = 12
        elif 585 <= vremya <= 639:
            key.add(matan)
            x = 11
        elif 640 <= vremya <= 694:
            if podgruppa == '1':
                key.add(azamat)
                x = 3
            elif podgruppa == '2':
                t = False
        else:
            t = False
    elif day == 5:  # Суббота
        if 500 <= vremya <= 584:
            key.add(terver)
            x = 13
        elif 585 <= vremya <= 639:
            key.add(vvedenie)
            x = 14
        elif 640 <= vremya <= 694:
            if podgruppa == '1':
                key.add(vvedenie)
                x = 15
            elif podgruppa == '2':
                t = False
        elif 695 <= vremya <= 745:
            if podgruppa == '1':
                t = False
            elif podgruppa == '2':
                key.add(vvedenie)
                x = 15
        else:
            t = False
    else:
        t = False

    if not z:
        bot.send_message(message.chat.id, config.no_podgrupp, parse_mode='HTML')
    elif not t:
        bot.send_message(message.chat.id, config.chill)
    else:
        bot.send_message(message.chat.id, config.para[x], reply_markup=key)


@bot.message_handler(func=lambda message: message.text.lower() == 'полный список пар')
def full_list(message):
    bot.send_message(message.chat.id, config.spisok, parse_mode='MarkdownV2')


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

    bot.send_message(call.message.chat.id, text=config.helpp, reply_markup=dai, parse_mode='HTML')


if __name__ == '__main__':
    bot.infinity_polling()


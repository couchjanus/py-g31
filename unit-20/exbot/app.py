# 

# -*- coding: utf-8 -*-
import telebot
import pytz
import datetime
import json
import traceback

# import exbot.config as config
# import exbot.api as api
# from exbot import GREETINGS, HELP_MESSAGES, EMOJI_UP, EMOJI_DOWN

import config
import api
from helpers import GREETINGS, HELP_MESSAGES, EMOJI_UP, EMOJI_DOWN

P_TIMEZONE = pytz.timezone(config.TIMEZONE)
TIMEZONE_COMMON_NAME = config.TIMEZONE_COMMON_NAME

# Створимо бот за допомогою бібліотеки pyTelegramBotAPI. 

# Створіть екземпляр класу TeleBot. Для цього вам слід передати токен у конструктор:

bot = telebot.TeleBot(config.TOKEN)

# bot = telebot.TeleBot(config.TOKEN, parse_mode=None)
# You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'welcome', 'hello'])
def send_welcome(message):
    bot.reply_to(message, GREETINGS)


@bot.message_handler(commands=['help'])
def send_help(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
    telebot.types.InlineKeyboardButton(
        'Message for developer', url='https://t.me/couchjanus'
        )
    )
    bot.reply_to(message, HELP_MESSAGES, reply_markup=keyboard)


@bot.message_handler(commands=['exchange'])
def send_exchange(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('USD', callback_data='get-USD'), telebot.types.InlineKeyboardButton('EUR', callback_data='get-EUR'))

    bot.reply_to(message, 'Click on the currency of choice:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('get-'):
        get_ex_callback(query)

def get_ex_callback(query):
    bot.answer_callback_query(query.id)
    send_exchange_result(query.message, query.data[4:])
    
def send_exchange_result(message, ex_code):
    bot.send_chat_action(message.chat.id, 'typing')
    ex = api.get_exchange(ex_code)
    bot.send_message(
        message.chat.id, serialize_ex(ex),
        reply_markup=get_update_keyboard(ex),
        parse_mode='HTML'
        )
def get_update_keyboard(ex):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(telebot.types.InlineKeyboardButton('Update', callback_data=json.dumps(
        {
        't': 'u', 
        'e': {
            'b': ex['buy'],
            's': ex['sale'],
            'c': ex['ccy']
            }
        }
    )
    .replace(' ', '')), 
    telebot.types.InlineKeyboardButton('Share', switch_inline_query=ex['ccy'])
    )
    return keyboard


def serialize_ex(ex_json, diff=None):
    result = f'''<b>{ex_json['base_ccy']} -> {ex_json['ccy']}:</b>\n\nBuy: {ex_json['buy']}'''
    if diff:
        result += f''' {serialize_exchange_diff(diff['buy_diff'])}\nSell: {ex_json['sale']} {serialize_exchange_diff(diff['sale_diff'])}\n'''
    else:
        result += f"\nSell: {ex_json['sale']}\n"
    return result

def serialize_exchange_diff(diff):
    result = ''
    if diff > 0:
        result = f'({str(diff)} {EMOJI_UP})'
    elif diff < 0:
        result = f'({str(diff)[1:]} {EMOJI_DOWN})'
    return result

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.infinity_polling()


# -*- coding: utf-8 -*-

import os
import time
import telebot
import config


bot = telebot.TeleBot(config.token)

# @bot.message_handler(commands=['text'])
# @bot.message_handler(content_types=['text'])
# def start_message(message):
#     #markup = telebot.types.InlineKeyboardMarkup()
#     tre = telebot.types.InlineKeyboardButton("Open", url="https://www.youtube.com/")
#     markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
#     btn = telebot.types.KeyboardButton('1111')
#     btn1 = telebot.types.KeyboardButton('hhhhh')
#     btn2 = telebot.types.LabeledPrice('price',2000)
#     markup.add(btn1,btn,btn2)
#     get_message = message.text.strip().lower()
#     if get_message =='hhhhh':
#         final_message = 'YES'
#
#     bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/'+file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
            time.sleep(3)
            print('-1-')
    print('-final-')


if __name__ == '__main__':
     bot.infinity_polling()



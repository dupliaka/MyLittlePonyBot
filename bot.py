import time

import schedule
import telebot

import config
import ponyImgParser

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "This is a bot for My little pony fan art notification per hour."
                                      "/start command to start mlp art subscription."
                                      "/more to send next pony art")


def publish_pony(message):
    bot.send_photo(message.chat.id, ponyImgParser.get_pony_img_url())


@bot.message_handler(commands=['start'])
def handle_start(message):
    publish_pony(message)
    schedule.every().hour.do(publish_pony, message)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    bot.polling(none_stop=True)

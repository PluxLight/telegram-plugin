"""
====================================
 :mod:`your.demo.helloworld`
====================================
.. moduleauthor:: Your Name <user@modify.me>
.. note::

Description
===========
Your Demo plugin module sample
"""
# Authors
# ===========
#
# * Your Name
#
# Change Log
# --------
#
#  * [2019/03/08]
#     - add icon
#  * [2018/10/28]
#     - starting

################################################################################
import sys
from alabs.common.util.vvargs import ModuleContext, func_log, \
    ArgsError, ArgsExit, get_icon_path
import os

import telegram
from telegram.ext import Filters, Updater, MessageHandler
from PIL import ImageGrab


bot_token = ''
chat_id = ''
sel = 0
ect = 0


################################################################################
def bot_idle():
    updater = Updater(bot_token, use_context=True)
    message_handler = MessageHandler(Filters.text,
                                     get_message)  # 메세지를 받았을 때 동작 할 것들
    updater.dispatcher.add_handler(message_handler)
    updater.start_polling()


def get_message(update, context):
    reply_markup = telegram.ReplyKeyboardRemove() # User Button Delete
    global sel
    global ect

    if update.message.text == 'yes' or update.message.text == 'Yes':
        ect = 1
        sel = 1
        context.bot.send_message(chat_id=chat_id, text='Continue',
                                 reply_markup=reply_markup)

    elif update.message.text == 'No':
        ect = 2
        sel = 1
        context.bot.send_message(chat_id=chat_id, text='STOP',
                                 reply_markup=reply_markup)

    os._exit(0)


def send_message(check_num, text_msg=''):
    bot = telegram.Bot(token=bot_token)
    if check_num==0: #only send message
        bot.sendMessage(chat_id=chat_id, text=text_msg)

    else: #Scenario control
        custom_keyboard = [['Yes', 'No']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)

        bot.send_message(chat_id=chat_id, text='Yes or No',
                         reply_markup=reply_markup)


def send_screenshot():
    bot = telegram.Bot(token=bot_token)
    img = ImageGrab.grab()
    img.save('screenshot.png')
    bot.send_photo(chat_id=chat_id, photo=open('screenshot.png', 'rb'), timeout=120)


def print_yes_no(select):
    if select==1:
        sys.stdout.write("yes") #Continue Scenario

    elif select==2:
        sys.stdout.write("no") #Stop Scenario


@func_log
def telegram_func(mcxt, argspec):
    """
    plugin job function
    :param mcxt: module context
    :param argspec: argument spec
    :return: True
    """
    mcxt.logger.info('>>>starting...')

    global bot_token, chat_id
    global sel, ect

    bot_token = argspec.bot_token
    chat_id = argspec.chat_id

    if argspec.screenshot is True:
        send_screenshot()

    send_message(0, argspec.message)

    if argspec.control is True:
        send_message(1)
        bot_idle()

        loop_num = 0

        while loop_num == 0:
            loop_num = sel

        value = ect

        print_yes_no(value)


    mcxt.logger.info('>>>end...')

    return 0


################################################################################
def _main(*args):
    """
    Build user argument and options and call plugin job function
    :param args: user arguments
    :return: return value from plugin job function
    """
    with ModuleContext(
        owner='jeon',
        group='telegram',
        version='2.0',
        platform=['windows', 'darwin', 'linux'],
        output_type='text',
        display_name='Telegram Plugin',
        icon_path=get_icon_path(__file__),
        description='Telegram Bot Plugin',
    ) as mcxt:
        # ##################################### for app dependent parameters
        mcxt.add_argument('bot_token',
                          display_name='Bot Token',
                          help='telegram bot token')
        mcxt.add_argument('chat_id',
                          display_name='Chat ID',
                          help='telegram Chat ID')
        mcxt.add_argument('message',
                          display_name='Message',
                          help='telegram bot send message')
        mcxt.add_argument('--screenshot',
                          display_name='Send Screenshot',
                          action='store_true',
                          help='telegram bot send screenshot')
        mcxt.add_argument('--control',
                          display_name='Scenario Control',
                          action='store_true',
                          help='yes or no button')
        argspec = mcxt.parse_args(args)
        return telegram_func(mcxt, argspec)


################################################################################
def main(*args):
    try:
        return _main(*args)
    except ArgsError as err:
        sys.stderr.write('Error: %s\nPlease -h to print help\n' % str(err))
    except ArgsExit as _:
        pass

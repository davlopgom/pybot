#!/usr/bin/env python
"""
 battletags.py  Battlenet user list.
 Author:        Rael Garcia <self@rael.io>
 Date:          0692016
 Tested on:     Python 3 / OS X 10.11.5
"""

import re
import random
import os

from telegram import InlineQueryResultArticle, ForceReply, \
        ParseMode, InputTextMessageContent, Emoji, \
        InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import Updater, InlineQueryHandler, CommandHandler, \
    MessageHandler, CallbackQueryHandler, Filters

"""Function to log per day"""
"""/start"""
import time
import logging
import logging.handlers
import win_unicode_console

win_unicode_console.enable(use_unicode_argv=True)
now = time.localtime(time.time())
strdate = time.strftime("%d%m%y", now)
log_file_name = './logs/pybot_'+strdate+'.log'
logging_level = logging.INFO

try:
    # set TimedRotatingFileHandler for root
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
    # use very short interval for this example, typical 'when' would be 'midnight' and no explicit interval
    handler = logging.handlers.TimedRotatingFileHandler(log_file_name, when="midnight")
    handler.setFormatter(formatter)
    logger = logging.getLogger() # or pass string to give it a name
    logger.addHandler(handler)
    logger.setLevel(logging_level)

except KeyboardInterrupt:
    # handle Ctrl-C
    logging.warn("Cancelled by user")
except Exception as ex:
    # handle unexpected script errors
    logging.exception("Unhandled error\n{}".format(ex))
    raise
finally:
    # perform an orderly shutdown by flushing and closing all handlers; called at application exit and no further use of the logging system should be made after this call.
    logging.shutdown()
"""/end"""


from subprocess import check_output
from importlib import reload

def update_yourself(bot, update):

    output = check_output(["git", "pull"]).decode("utf-8")
    reload(brain)

    logger.info(output)
    bot.sendMessage(update.message.chat_id, text=output)

def escape_markdown(text):
    """Helper function to escape telegram markup symbols"""
    escape_chars = '\*_`\['
    return re.sub(r'([%s])' % escape_chars, r'\\\1', text)

def error(bot, update, error):
    """Error handler function"""
    logger.warn('Update "%s" caused error "%s"' % (update, error))

import brain

def hear(bot, update):
    """Function to handle text messages"""
    thoughts = brain.ears(update.message.text)

    remember(bot, update)
    if thoughts: speak(bot, update, thoughts)

    m = update.message

import requests

def speak(bot, update, thoughts):
    """Function to handle bot responses"""
    logger.info('I\'ve got something to say.')
    for words in thoughts:
        r= re.search(r'\'file_id\': \'(.*?)\'.*', words)
        if os.path.isfile(words):
            show(bot, update, words, 'file')
        elif words.startswith('http'):
            show(bot, update, words, 'url')
        elif r:
            show(bot, update, r.group(1),'tarchive')
        else:
            bot.sendMessage(update.message.chat_id, text=words)


def show(bot, update, stuff, type):
    """Function to handle bot responses when he need more than words"""
    logger.info('I\'ve got something to show.')
    try:
        if type == 'file':
            thing = open(stuff, 'rb')
        elif type == 'url':
            if requests.get(stuff).status_code == 200:
                thing = stuff
            else:
                logger.warn("%s is not available." % stuff)
        else:
            thing = stuff

        if thing and stuff.lower().endswith(('.png', '.jpg', '.jpeg')):
            bot.sendPhoto(update.message.chat_id, photo=thing)
        elif thing:
            bot.sendDocument(update.message.chat_id, document=thing)

    except:
        logger.warn("I can't show the %s" % stuff)
        bot.sendMessage(update.message.chat_id, text=stuff)

def view(bot, update):
    """Function to handle photo messages"""
    thoughts = brain.eyes(bot.getFile(update.message.photo[-1].file_id).file_path)

    remember(bot, update)
    if thoughts: speak(bot, update, thoughts)

def event_response(bot, update):
    """Function to handle text messages"""
    if update.message.new_chat_member is not None:
        logger.info('New member')
        thoughts = brain.respond(update.message.text, 'member_join')

    if update.message.left_chat_member is not None:
        logger.info('Member left')
        thoughts = brain.respond(update.message.text, 'member_left')

    remember(bot, update)
    if thoughts is not None: speak(bot, update, thoughts)

def docid(bot, update):
    """Function to get the document id stored on bot"""
    m = update
    r= re.search(r'\'file_id\': \'(.*?)\',', str(m))
    bot.sendMessage(update.message.chat_id, text=r.group(1))

def dynmenu(bot, update):
    """Function to print a dynamic menu"""
    keyboard = []
    keyboard.append([])
    values = brain.menu(update.message.from_user.id) #Read the main menu
    i=0
    c=0
    for row in values: #Build the menu
        keyboard[i].append(InlineKeyboardButton(row[0], callback_data=row[1]))
        c=c+1
        if c != 0 and c % 3==0 and row != values[-1]: #Modify c % 3 by c % number of columns per line to print
            i=i+1
            keyboard.append([])

    keyboard.append([InlineKeyboardButton("<- Salir", callback_data='exit')])

    reply_markup = InlineKeyboardMarkup(keyboard)

    r=bot.sendMessage(update.message.chat_id, text='<b>Menú de opciones:</b>',parse_mode=ParseMode.HTML, reply_markup=reply_markup)

    #brain.menu_control('create', update.message.from_user.id, update.message.chat_id, r.message_id)  #Give the control of menu to owner


def button(bot, update):
    """Function to edit the dynamic menu by push buttons of it"""
    query = update.callback_query
    #check = brain.menu_control('check', query.from_user.id, query.message.chat_id, query.message.message_id)  #Give the control of menu to owner
    #if check > 0:
    
    if query.data=='exit':
        bot.editMessageText(text='Cancelado', chat_id=query.message.chat_id, message_id=query.message.message_id)
    elif query.data=='home':
        keyboard = []
        keyboard.append([])
        values = brain.menu(query.from_user.id)
        i=0
        c=0
        for row in values: #Build the submenu
            keyboard[i].append(InlineKeyboardButton(row[0], callback_data=row[1]))
            c=c+1
            if c != 0 and c % 3==0 and row != values[-1]: #Modify c % 3 by c % number of columns per line to print
                i=i+1
                keyboard.append([])

        keyboard.append([InlineKeyboardButton("<- Salir", callback_data='exit')])

        reply_markup = InlineKeyboardMarkup(keyboard)

        bot.editMessageText('<b>Menú de opciones:</b>', parse_mode=ParseMode.HTML, reply_markup=reply_markup, chat_id=query.message.chat_id, message_id=query.message.message_id)
    elif re.search(r'^_.*', query.data):
        keyboard = []
        keyboard.append([])
        values = brain.submenu(query.data, query.from_user.id)
        i=0
        c=0
        for row in values: #Build the submenu
            if re.search(r'^http:|https:.*', row[1]):
                keyboard[i].append(InlineKeyboardButton(row[0], url=row[1]))
            else:
                keyboard[i].append(InlineKeyboardButton(row[0], callback_data=row[1]))
            c=c+1
            if c != 0 and c % 3==0 and row != values[-1]: #Modify c % 3 by c % number of columns per line to print
                i=i+1
                keyboard.append([])

        keyboard.append([InlineKeyboardButton("<< Atrás", callback_data='home')])

        reply_markup = InlineKeyboardMarkup(keyboard)
				
        bot.editMessageText(text='<b>Menú de opciones:</b>',parse_mode=ParseMode.HTML, reply_markup=reply_markup,
								chat_id=query.message.chat_id,
								message_id=query.message.message_id)
    else:
        thoughts = brain.ears(query.data)
        if thoughts: speak(bot, query, thoughts)


def remember(bot, update):
    m = update.message
    brain.remember(m.date, m.chat_id, m.from_user.id, m.text)

def main():
    updater = Updater(os.environ['TELEGRAM_TOKEN'])
    dp = updater.dispatcher
    logger.info('Bot %s up and ready!' % (dp.bot.username))

    # Message handlers
    dp.add_handler(MessageHandler([Filters.text], hear))
    dp.add_handler(MessageHandler([Filters.photo], view))
    dp.add_handler(MessageHandler([Filters.status_update], event_response))

    # Command definitions
    dp.add_handler(CommandHandler("battletags", hear))
    dp.add_handler(CommandHandler("groups", groups_hardcoded))
    dp.add_handler(CommandHandler("trophies", hear))
    dp.add_handler(CommandHandler("update_yourself", update_yourself))
    dp.add_handler(CommandHandler('menu', dynmenu))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler([Filters.document], docid))
    dp.add_handler(MessageHandler([Filters.sticker], docid)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()

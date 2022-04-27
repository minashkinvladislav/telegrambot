import logging
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext

updater = Updater(token='1742810600:AAF0bFtyadoldVbZRk4vJDz4KjZ6DCn9dUA', use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def gulyaev(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Monkey, Monkey, Monkey")
gulyaev_handler = CommandHandler('gulyaev', gulyaev)
dispatcher.add_handler(gulyaev_handler)


def veprikov(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Пиво, пивас, пивасик...мммм...")
veprikov_handler = CommandHandler('veprikov', veprikov)
dispatcher.add_handler(veprikov_handler)

updater.start_polling()

# from telegram.ext import MessageHandler

# def echo(update: Update, context: CallbackContext):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
#
# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# dispatcher.add_handler(echo_handler)
#
# def caps(update: Update, context: CallbackContext):
#     text_caps = ' '.join(context.args).upper()
#     context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
#
# caps_handler = CommandHandler('caps', caps)
# dispatcher.add_handler(caps_handler)
#
# from telegram import InlineQueryResultArticle, InputTextMessageContent
# def inline_caps(update: Update, context: CallbackContext):
#     query = update.inline_query.query
#     if not query:
#         return
#     results = []
#     results.append(
#         InlineQueryResultArticle(
#             id=query.upper(),
#             title='Caps',
#             input_message_content=InputTextMessageContent(query.upper())
#         )
#     )
#     context.bot.answer_inline_query(update.inline_query.id, results)
#
# from telegram.ext import InlineQueryHandler
# inline_caps_handler = InlineQueryHandler(inline_caps)
# dispatcher.add_handler(inline_caps_handler)
#
# def unknown(update: Update, context: CallbackContext):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
#
# unknown_handler = MessageHandler(Filters.command, unknown)
# dispatcher.add_handler(unknown_handler)





from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from decouple import config

BOT_TOKEN = config('BOT_TOKEN')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Отправьте сообщение.')

def echo(update: Update, context: CallbackContext) -> None:
    message = update.message.text
    if message.isdigit():
        response = int(message) ** 2
    else:
        response = message
    update.message.reply_text(response)

def send_file(update: Update, context: CallbackContext) -> None:
    with open('path_to_file', 'rb') as file:
        update.message.reply_document(document=file)

def main() -> None:
    updater = Updater(BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dispatcher.add_handler(CommandHandler("sendfile", send_file))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


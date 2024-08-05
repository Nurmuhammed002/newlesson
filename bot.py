from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from decouple import config

# Получение токена из .env файла
BOT_TOKEN = config('BOT_TOKEN')

# Обработчик команды /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет! Отправьте сообщение.')

# Обработчик текстовых сообщений
async def echo(update: Update, context: CallbackContext) -> None:
    message = update.message.text
    if message.isdigit():
        response = int(message) ** 2
    else:
        response = message
    await update.message.reply_text(response)

# Функция для отправки файлов
async def send_file(update: Update, context: CallbackContext) -> None:
    with open('path_to_file', 'rb') as file:
        await update.message.reply_document(document=file)

# Главная функция для настройки и запуска бота
def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавление обработчиков
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(CommandHandler("sendfile", send_file))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()

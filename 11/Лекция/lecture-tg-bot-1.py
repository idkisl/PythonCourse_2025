from telegram.ext import Application, MessageHandler, CommandHandler, filters

BOT_TOKEN = "8576739672:AAFHWW8aCHF46Hvtp3rnKQ6lUk8Lq4MFnAw"


async def echo(update, context):
    print(update.message.text, update.message.chat.first_name)
    await update.message.reply_text(f"Ты мне написал {update.message.text}, а я тебе напишу удачи!")


async def start(update, context):
    await update.message.reply_text(f"Привет, {update.message.chat.first_name}. Давай работать вместе!")


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    start_handler = CommandHandler("start", start)
    application.add_handler(text_handler)
    application.add_handler(start_handler)
    application.run_polling()


if __name__ == "__main__":
    main()



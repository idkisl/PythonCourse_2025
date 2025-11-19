from telegram.ext import Application, MessageHandler, CommandHandler, filters

BOT_TOKEN = "8576739672:AAFHWW8aCHF46Hvtp3rnKQ6lUk8Lq4MFnAw"

users = {}

async def echo(update, context):
    print(update.message.text, update.message.chat.first_name, update)
    await update.message.reply_text(f"Ты мне написал {update.message.text}, а я тебе напишу удачи!")


async def start(update, context):
    id = update.message.from_user.id
    if id in users:
        await update.message.reply_text(f"{update.message.chat.first_name}, ты со мной уже здоровался!")
    else:
        await update.message.reply_text(f"Привет, {update.message.chat.first_name}. Давай работать вместе!")
        users[id] = 1

async def help(update, context):
    await update.message.reply_text(f"Ты можешь со мной поздороваться, а можешь узнать свой номер!")

async def increase(update, context):
    id = update.message.from_user.id
    if id in users:
        users[id] += 1
        await update.message.reply_text(f"Это уже {users[id]} обращение. Не устал ли?")
    else:
        await update.message.reply_text(f"Сначала зарегистрируйся по команде /start")


def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("increase", increase))

    application.run_polling()


if __name__ == "__main__":
    main()



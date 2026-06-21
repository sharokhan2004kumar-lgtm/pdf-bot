from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8644397786:AAG9oHc2aXOgsQZ7YCeLXeO4SvFe7fOIn2U"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بك، البوت شغال بنجاح 🚀"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()

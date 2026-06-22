import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أرسل لي ملف PDF 📚"
    )

async def handle_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("وصلتني رسالة 📩")

    document = update.message.document

await update.message.reply_text("⏳ جاري تحميل الملف...")

file = await context.bot.get_file(document.file_id)

await file.download_to_drive("book.pdf")

await update.message.reply_text(
    f"✅ تم تحميل الملف: {document.file_name}"
)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(
    MessageHandler(filters.Document.ALL, handle_pdf)
)

app.run_polling()

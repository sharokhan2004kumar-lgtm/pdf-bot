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
    document = update.message.document

    await update.message.reply_text("📥 جاري استلام الملف...")

    file = await context.bot.get_file(document.file_id)
    await file.download_to_drive("book.pdf")

    await update.message.reply_text("📖 جاري استخراج النص...")

    import pdfplumber

    text = ""

    with pdfplumber.open("book.pdf") as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    if not text.strip():
        await update.message.reply_text("❌ لم أتمكن من استخراج النص من الملف")
        return

    await update.message.reply_text("🎤 جاري تحويل النص إلى صوت...")

    from gtts import gTTS

    tts = gTTS(text=text[:5000], lang="ar")
    tts.save("book.mp3")

    await update.message.reply_audio(
        audio=open("book.mp3", "rb"),
        title="الكتاب الصوتي"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(
    MessageHandler(filters.Document.ALL, handle_pdf)
)

app.run_polling()

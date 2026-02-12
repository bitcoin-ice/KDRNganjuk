from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

async def reply_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot hidup dan siap!")

def main():
    app = ApplicationBuilder().token("8206077264:AAF0zPrJMGDXXRsiR-yJ7qT0DK2G8Ll5I24").build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_text))
    app.run_polling()

if __name__ == "__main__":

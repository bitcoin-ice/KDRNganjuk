from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Fungsi balas pesan
async def reply_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot hidup dan siap!")

# Fungsi main untuk menjalankan bot
def main():
    import os
    token = os.getenv("BOT_TOKEN")  # Ambil token dari Environment Variable
    if not token:
        print("Error: BOT_TOKEN belum diset!")
        return

    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_text))
    print("Bot berjalan...")  # Untuk log Railway
    app.run_polling()

# Poin penting: harus ada 2 underscore sebelum & sesudah
if __name__ == "__main__":
    main()

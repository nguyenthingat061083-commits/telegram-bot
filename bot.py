import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = "8727406351:AAHS47lEXskpWFDIkyWZxMDO9XP7oKL7mNI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot đang chạy! Gõ /ping để kiểm tra.")

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong!")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping))
    
    print("🚀 Bot đã sẵn sàng!")
    app.run_polling()

if __name__ == "__main__":
    main()

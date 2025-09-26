import json
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Load ENV token
TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_ID = 7918600537  # tumhara admin ID

# Load database
with open("videos.json", "r", encoding="utf-8") as f:
    VIDEO_DB = json.load(f)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome! Send me a video title and I’ll find the link for you.")

# Search handler
async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.strip().lower()
    results = [v for v in VIDEO_DB if query in v["title"].lower()]

    if results:
        for video in results:
            msg = f"🎬 *{video['title']}*\n\n▶️ [Stream Link]({video['stream']})\n⬇️ [Download Link]({video['download']})"
            await update.message.reply_markdown(msg)
    else:
        await update.message.reply_text("❌ No results found!")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

    app.run_polling()

if __name__ == "__main__":
    main()

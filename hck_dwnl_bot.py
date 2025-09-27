import json
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Load ENV token
TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_ID = 7918600537  # tumhara admin ID

# Load database (videos.json should have "thumbnail" field also)
with open("videos.json", "r", encoding="utf-8") as f:
    VIDEO_DB = json.load(f)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome! Send me a video title and I’ll find the link with thumbnail!")

# Search handler
async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text.strip().lower()
    results = [v for v in VIDEO_DB if query in v["title"].lower()]

    if results:
        for video in results:
            caption = (
                f"🎬 *{video['title']}*\n\n"
                f"▶️ [Stream Link]({video['stream']})\n"
                f"⬇️ [Download Link]({video['download']})"
            )

            # If thumbnail exists → send with photo
            if "thumbnail" in video and video["thumbnail"]:
                await context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo=video["thumbnail"],
                    caption=caption,
                    parse_mode="Markdown"
                )
            else:
                # Fallback without thumbnail
                await update.message.reply_markdown(caption)
    else:
        await update.message.reply_text("❌ No results found!")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()

import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 স্বাগতম!\n\n"
        "গেম খেলতে /play লিখুন।"
    )

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎲 গেম শুরু হয়েছে!\n"
        "শিগগিরই এখানে আসল গেম যোগ করা হবে।"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("play", play))

print("Bot Running...")

app.run_polling()

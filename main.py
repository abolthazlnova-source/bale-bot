import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

app = Flask(__name__)

@app.route("/")
def home():
    return "Bale Bot is alive"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

TOKEN = os.environ.get("BALE_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات بله فعاله")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("دستورات:\n/start\n/help")

def main():
    threading.Thread(target=run_web, daemon=True).start()

    application = Application.builder() \
        .token(TOKEN) \
        .base_url("https://tapi.bale.ai/bot") \
        .build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_cmd))

    print("Bale Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()

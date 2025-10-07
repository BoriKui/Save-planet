import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


links = [
    "https://ru.wikipedia.org/wiki/Глобальное_потепление",
    "https://trends.rbc.ru/trends/green/641402fe9a7947520b87e078",
    "https://journal.sovcombank.ru/esg/globalnoe-poteplenie-prichini-i-posledstviya",
    "https://ria.ru/20251006/klimat-2046676016.html",
    "https://rg.ru/2023/11/07/kak-prostoj-chelovek-mozhet-povliiat-na-globalnoe-poteplenie.html"
    
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Используй команду /getlink, чтобы получить случайную статью о глобальном потеплении.")


async def get_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    link = random.choice(links)
    await update.message.reply_text(link)


def main():
    
    TOKEN = "8226728454:AAHp9AMbibrWqyw-0IJrF56qaT8AVJLAerM"
    
    
    logging.basicConfig(level=logging.INFO)
    
    
    app = ApplicationBuilder().token(TOKEN).build()
    
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("getlink", get_link))
    
    
    app.run_polling()

if __name__ == '__main__':
    main()

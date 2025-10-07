import random
import logging
from telegram.ext import ApplicationBuilder, CommandHandler


TOKEN = ""


links = [
    "https://ru.wikipedia.org/wiki/Глобальное_потепление",
    "https://trends.rbc.ru/trends/green/641402fe9a7947520b87e078",
    "https://journal.sovcombank.ru/esg/globalnoe-poteplenie-prichini-i-posledstviya",
    "https://ria.ru/20251006/klimat-2046676016.html",
    "https://rg.ru/2023/11/07/kak-prostoj-chelovek-mozhet-povliiat-na-globalnoe-poteplenie.html"
]

logging.basicConfig(level=logging.INFO)

async def start(update, context):
    await update.message.reply_text(
        "Привет! Я бот о глобальном потеплении.\n"
        "Команды:\n"
        "/getlink - получить случайную статью\n"
        "/addlink <ссылка> - добавить новую ссылку\n"
        "/help - помощь"
    )

async def help_command(update, context):
    await update.message.reply_text(
        "Доступные команды:\n"
        "/start - приветствие\n"
        "/getlink - получить случайную статью\n"
        "/addlink <ссылка> - добавить новую ссылку\n"
        "/help - показать команды"
    )

async def get_link(update, context):
    if links:
        link = random.choice(links)
        await update.message.reply_text(link)
    else:
        await update.message.reply_text("Ссылки еще не добавлены.")

async def add_link(update, context):
    new_link = ' '.join(context.args)
    if new_link:
        links.append(new_link)
        await update.message.reply_text(f"Ссылка добавлена: {new_link}")
    else:
        await update.message.reply_text("Пожалуйста, укажите ссылку после команды /addlink.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("getlink", get_link))
    app.add_handler(CommandHandler("addlink", add_link))
    app.run_polling()

if __name__ == '__main__':
    main()

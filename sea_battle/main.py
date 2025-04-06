# Импортируем необходимые классы.
import logging
from telegram.ext import Application, MessageHandler, filters
from config import BOT_TOKEN
from telegram.ext import CommandHandler

from telegram import Update
from telegram.ext import ContextTypes

# Логирование
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Игра: заменить на ваш SHORT NAME из BotFather
GAME_SHORT_NAME = 'Sea battle bot'  # 👉 сюда вставь своё короткое имя игры

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_game(game_short_name=GAME_SHORT_NAME)

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()

if __name__ == "__main__":
    main()
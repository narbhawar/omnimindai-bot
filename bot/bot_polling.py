# Simple polling entry for local dev/testing
import os, logging
from aiogram import Bot, Dispatcher, executor
from bot.handlers import register_handlers

logging.basicConfig(level=logging.INFO)
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise SystemExit("Set TELEGRAM_BOT_TOKEN in env for polling mode")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

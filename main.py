# Entrypoint for webhook mode (aiogram + minimal FastAPI health endpoint)
import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.utils.executor import start_webhook
from backend.ai_client import init_openai_client
from bot.handlers import register_handlers

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("omnimind_main")

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    log.critical("Missing TELEGRAM_BOT_TOKEN env var")
    raise SystemExit("TELEGRAM_BOT_TOKEN required")

RENDER_EXTERNAL_URL = os.getenv("RENDER_EXTERNAL_URL") or os.getenv("WEBHOOK_HOST")
WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URL = (RENDER_EXTERNAL_URL.rstrip("/") + WEBHOOK_PATH) if RENDER_EXTERNAL_URL else None

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# register handlers
register_handlers(dp)

async def on_startup(dispatcher):
    init_openai_client()
    if WEBHOOK_URL:
        await bot.set_webhook(WEBHOOK_URL)
        log.info(f"Webhook set to {WEBHOOK_URL}")
    else:
        log.warning("WEBHOOK_URL not configured; set RENDER_EXTERNAL_URL env var to auto-register webhook.")

async def on_shutdown(dispatcher):
    try:
        await bot.delete_webhook()
    except Exception:
        pass

if __name__ == "__main__":
    WEBAPP_HOST = "0.0.0.0"
    WEBAPP_PORT = int(os.getenv("PORT", "10000"))
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )

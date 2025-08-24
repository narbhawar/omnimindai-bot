# OmniMind AI — Multilingual Recipe, Fitness & Nutrition Telegram Bot

Production-ready template repository for OmniMind AI: multilingual, webhook-first Telegram bot + FastAPI backend, Postgres storage, OpenAI integration, and deployment-ready assets (Docker/Render).

## Features
- Webhook-first Telegram bot (aiogram)
- FastAPI backend endpoints for vision/speech/recipes
- Robust OpenAI client wrapper (supports older & new SDK shapes)
- PostgreSQL via asyncpg (migrations included)
- Multilingual language detection (langdetect)
- Admin CLI for broadcasts & exports
- Dockerfile & docker-compose for local testing
- Render deployment instructions

## Quickstart (dev)
1. Copy `.env.example` → `.env` and fill values.
2. Build virtualenv & install:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3. Initialize DB (if using Postgres) by running the SQL in `migrations/01_init.sql` or configure Supabase/Render Postgres.
4. Start the app (dev webhook-testing with ngrok or use polling locally):
```bash
# For local dev testing you may prefer polling: run bot/bot_polling.py
python bot/bot_polling.py
# Or run the webhook server (suitable for Render):
python main.py
```
5. Set Telegram webhook (replace placeholders):
```bash
TOKEN="<your-token>"
DOMAIN="https://your-render-app.onrender.com"
curl -X POST "https://api.telegram.org/bot${TOKEN}/setWebhook" -F "url=${DOMAIN}/webhook/${TOKEN}"
```

## Deploy to Render (high-level)
- Create Web Service from GitHub repo.
- Set Environment Variables:
  - TELEGRAM_BOT_TOKEN, DATABASE_URL, OPENAI_API_KEY, RENDER_EXTERNAL_URL (optional), ADMIN_IDS
- Start command: `python main.py` (or use `uvicorn backend.main:app --host 0.0.0.0 --port $PORT` if splitting services)
- Redeploy and check logs.

## Security & Privacy Notes
- DO NOT commit real API keys to the repo — use Render/Heroku/GitHub secrets.
- Body-transformation and user images require explicit consent — see `docs/privacy.md` for required flows.

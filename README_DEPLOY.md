# Deploy guide (short)

1. Push this repo to GitHub.
2. Create Render Web Service → connect to repo.
3. Set env vars: TELEGRAM_BOT_TOKEN, DATABASE_URL, OPENAI_API_KEY, RENDER_EXTERNAL_URL
4. Deploy. Ensure service logs show 'Webhook set to ...'
5. Set webhook (if not auto):
   curl -X POST "https://api.telegram.org/bot${TOKEN}/setWebhook" -F "url=${DOMAIN}/webhook/${TOKEN}"

# Simple handler implementations that call the AI client
from aiogram import types
from backend.ai_client import ask_ai
from langdetect import detect, LangDetectException

async def cmd_start(message: types.Message):
    await message.reply("🌍 OmniMind AI — multilingual recipes, fitness & nutrition. Try /recipe <ingredients> or /track <meal>")

async def cmd_recipe(message: types.Message):
    user_input = message.get_args() or "chicken, rice, salad"
    lang = 'en'
    try:
        lang = detect(user_input)
    except LangDetectException:
        lang = 'en'
    prompt = f"Create 3 concise recipes for: {user_input}. Include kcal estimates and 2-line steps each. Reply in language '{lang}'. Keep it short."
    reply = await ask_ai(prompt, lang)
    await message.reply(reply)

async def cmd_track(message: types.Message):
    meal = message.get_args() or "meal logged"
    # TODO: store in DB
    await message.reply(f"✅ Logged: {meal}")

async def fallback(message: types.Message):
    text = message.text or ''
    lang = 'en'
    try:
        lang = detect(text)
    except LangDetectException:
        lang = 'en'
    prompt = f"User said: {text}. Reply concisely in language '{lang}'."
    reply = await ask_ai(prompt, lang)
    await message.reply(reply)

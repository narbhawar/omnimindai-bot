# Register handlers and simple implementations
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram import Dispatcher
from bot.logic import cmd_start, cmd_recipe, cmd_track, fallback

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(cmd_recipe, commands=['recipe'])
    dp.register_message_handler(cmd_track, commands=['track','log'])
    dp.register_message_handler(fallback)

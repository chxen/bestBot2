from aiogram import Bot, types

from bot.settings import BOT_TOKEN, GOOGLE_CREDENTIALS_FILE

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)

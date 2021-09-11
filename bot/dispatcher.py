from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from . import bot

storage = MemoryStorage()
dispatcher = Dispatcher(bot, storage=storage)

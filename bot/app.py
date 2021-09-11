from datetime import datetime

from bot.loader import bot, db, dp
import aioschedule as schedule
import asyncio
import time

from bot.reminder import job


async def my_function():
    time = datetime.now()
    schedule.every().day.at("10:51").do(job)
    print()
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(dp):
    try:
        db.create_table_users()
        asyncio.create_task(my_function)
    except Exception as e:
        print(e)


async def send_message(id, text):
    await bot.send_message(id, text)


if __name__ == '__main__':
    from aiogram import executor, types
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_startup, on_startup=on_startup)

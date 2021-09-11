import aioschedule as schedule
import asyncio

from bot.reminder import job


async def my_function():
    schedule.every(1).minute.do(job)
    while True:
        await schedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(dp):
    asyncio.create_task(my_function())


if __name__ == '__main__':
    from aiogram import executor
    from bot.handlers import dispatcher

    print('App started!')
    executor.start_polling(dispatcher, on_startup=on_startup)
    print('App shut down!')

import sqlite3
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold, hlink
from datetime import datetime, date, timedelta
from bot.data.config import service, spreadsheet_id
from bot.loader import dp, db, bot
from aiogram.dispatcher.filters.state import StatesGroup, State
import aioschedule as schedule
import asyncio


class Test(StatesGroup):
    S1 = State()


async def send_message(id, text):
    await bot.send_message(id, text)

'''
async def job():
    for i in range(0, 1000):
        otvet1 = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range='A1:A900',
            majorDimension='ROWS'
        ).execute()

        lesson1 = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range='B1:B900',
            majorDimension='ROWS'
        ).execute()

        futured = datetime.now()
        if otvet1['values'][i][0] == futured.strftime("%d.%m.%Y %H:%M"):
            await send_message(int(db.get_id_group(groupi='1')[0]), f"Время пройти урок: {lesson1['values'][i][0]}")
        await asyncio.sleep(1)
'''
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    db.create_table_users()
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        print(err)

    await message.answer(text=f'Добро пожаловать в бот расписаний, <b>{message.from_user.full_name}</b>!\n' +
                         hbold("Пожалуйста пришли мне номер группы. Только цифру: 1, 2, 3.\n")
                              + "Таблица с расписанием доступна по " + hlink("ссылке",
                                                                             "https://docs.google.com/spreadsheets/d"
                                                                             "/1xT_P8rhQ7_0paAHbE-elHp0P-73en13Ms99d6tw-KVA/edit#gid=0"),
                         disable_web_page_preview=True)
    await Test.S1.set()


@dp.message_handler(state=Test.S1)
async def enter_group(message: types.Message, state: FSMContext):
    groupi = message.text
    if groupi == "1" or groupi == "2" or groupi == "3":
        db.update_group(groupi=groupi, id=message.from_user.id)
        user = db.select_user(id=message.from_user.id)
        await message.answer(f"Данные были обновлены. Запись в бд: {user}")

    else:
        await message.answer("Неверный номер группы. Вызовите команду /start еще раз и введите номер группы: 1, "
                             "2 или 3.")

    await asyncio.sleep(1)

    #print(f"hvhvm {db.get_id_group(groupi='1')[0]}")
    await state.finish()
